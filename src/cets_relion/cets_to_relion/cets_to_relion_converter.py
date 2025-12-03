"""Read CETS data and write a RELION movies file"""

from pathlib import Path
from typing import Union, List, Dict
from cets_data_model.models.models import MovieFrame
from gemmi import cif
from cets_relion.cets_to_relion.cets_reader import CetsReader


class CetsToRelionConverter(object):
    def __init__(self, input_file: Union[Path, str]):
        self.data = CetsReader(input_file)

    @staticmethod
    def get_dose_rate(frames: List[MovieFrame]):
        rate = frames[1].accumulated_dose - frames[0].accumulated_dose
        return rate

    @staticmethod
    def ts_master_file_basic_data(name: str) -> List[str]:
        # ToDo: This info will probably need to come from an AcquisitionData object of
        #  some sort in the CETS model
        ts_starfile_name = str(f"tilt_series/{name}.star")
        return [
            name,
            ts_starfile_name,
            "XXX_Voltage",
            "XXX_SphericalAberration",
            "XXX_AmplitudeContrast",
            "XXX_MicrographOriginalPixelSize",
            "XXX_TomoHand",
            "Optics1",
            "XXX_TomoTiltSeriesPixelSize",
            "XXX_EtomoDirectiveFile",
        ]

    def ts_file_data_from_frames(self) -> Dict[str, List[List[str]]]:
        data: Dict[str, List[List[str]]] = {}
        for name, movie_stack in self.data.movie_stacks.items():
            for stack in movie_stack:
                frames = stack.images
                vals = [
                    stack.path,
                    str(len(frames)),
                    str(frames[0].nominal_tilt_angle),
                    "XXX_TomoNominalStageTiltAngle",
                    str(frames[0].accumulated_dose - self.get_dose_rate(frames)),
                    "XXX_TomoNominalDefocus",
                ]
                if frames[0].ctf_metadata is not None and None not in [
                    frames[0].ctf_metadata.defocus_u,
                    frames[0].ctf_metadata.defocus_v,
                    frames[0].ctf_metadata.defocus_angle,
                ]:
                    u = frames[0].ctf_metadata.defocus_u
                    v = frames[0].ctf_metadata.defocus_v
                    vals.extend(
                        [
                            "XXX_CtfImage",
                            str(u),
                            str(v),
                            str(u - v),
                            str(frames[0].ctf_metadata.defocus_angle),
                            "XXX_CtfFigureOfMerit",
                            "XXX_CtfMaxResolution",
                            "XXX_CtfIceRingDensity",
                        ]
                    )

                # TODO: get the alignment data here and add it to vals
                #  if found

                if data.get(name) is None:
                    data[name] = [vals]
                else:
                    data[name].append(vals)
        return data

    def write_main_relion_ts_starfile(self) -> List[str]:
        """The movies import job is required for this"""
        main_starfile = cif.Document()
        main_block = main_starfile.add_new_block(name="global")
        main_loop = main_block.init_loop(
            prefix="_rln",
            tags=[
                "TomoName",
                "TomoTiltSeriesStarFile",
                "Voltage",
                "SphericalAberration",
                "AmplitudeContrast",
                "MicrographOriginalPixelSize",  # need to get from scale trans
                "TomoHand",
                "OpticsGroupName",
                "TomoTiltSeriesPixelSize",
                "EtomoDirectiveFile",
            ],
        )
        ts_dir = Path("tilt_series")
        ts_dir.mkdir(parents=True, exist_ok=True)

        added_tilt_series = []
        for name, movie_frames in self.data.movie_stacks.items():
            # if the binned pixel size is available get it here
            main_loop.add_row(self.ts_master_file_basic_data(name))
            added_tilt_series.append(name)
        main_starfile.write_file("tilt_series.star")
        return added_tilt_series

    def write_ts_starfiles(self):
        """Write a starfile for an individual tilt series in the tilt_series dir"""
        ts_dir = Path("tilt_series")
        ts_dir.mkdir(parents=True, exist_ok=True)
        ts_values = self.ts_file_data_from_frames()
        for ts_name, data in ts_values.items():
            ts_starfile = cif.Document()
            ts_block = ts_starfile.add_new_block(name=ts_name)
            tags = [
                "MicrographMovieName",
                "TomoTiltMovieFrameCount",
                "TomoNominalStageTiltAngle",
                "TomoNominalTiltAxisAngle",
                "MicrographPreExposure",
                "TomoNominalDefocus",
            ]
            if len(data[0]) == 14:
                tags.extend(
                    [
                        "CtfImage",
                        "DefocusU",
                        "DefocusV",
                        "CtfAstigmatism",
                        "DefocusAngle",
                        "CtfFigureOfMerit",
                        "CtfMaxResolution",
                        "CtfIceRingDensity",
                    ]
                )
            if len(data[0]) == 19:
                tags.extend(
                    [
                        "TomoXTilt",
                        "rlnTomoYTilt",
                        "rlnTomoZRot",
                        "rlnTomoXShiftAngst",
                        "rlnTomoYShiftAngst",
                    ]
                )

            ts_loop = ts_block.init_loop(
                prefix="_rln",
                tags=tags,
            )
            for line in data:
                ts_loop.add_row(line)
            sf_name = str(ts_dir / f"{ts_name}.star")
            ts_starfile.write_file(sf_name)
