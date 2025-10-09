"""Read CETS data and write a RELION movies file"""

from pathlib import Path
from typing import Union, List, Dict
from cets_data_model.models.models import MovieFrame
from gemmi import cif
from cets_relion.cets_reader import CetsReader


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
            "VOLTAGE-1",
            "SPHEREABB-1",
            "AMPCON-1",
            "APIX-1",
            "TOMOHAND-1",
            "Optics1",
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
                    "NOMTAA-1",
                    str(frames[0].accumulated_dose - self.get_dose_rate(frames)),
                    "NOMDEF-1",
                ]
                if data.get(name) is None:
                    data[name] = [vals]
                else:
                    data[name].append(vals)
        return data

    def get_ts_ctf_data(self) -> Dict[str, List[List[str]]]:
        return {}

    def get_ts_alignment_data(self) -> Dict[str, List[List[str]]]:
        return {}

    def write_main_relion_ts_starfile(self):
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
            ],
            # if the binned pixel size is available additional tag
            # _rlnTomoTiltSeriesPixelSize is needed
        )
        ts_dir = Path("tilt_series")
        ts_dir.mkdir(parents=True, exist_ok=True)

        for name, movie_frames in self.data.movie_stacks.items():
            # if the binned pixel size is available get it here
            main_loop.add_row(self.ts_master_file_basic_data(name))
        main_starfile.write_file("tilt_series.star")

    def write_ts_starfiles(self):
        """Write a starfile for an individual tilt series in the tilt_series dir"""
        ts_dir = Path("tilt_series")
        ts_dir.mkdir(parents=True, exist_ok=True)
        ts_values = self.ts_file_data_from_frames()
        ctf_data = self.get_ts_ctf_data()
        for ts in ctf_data:
            for n, frame in enumerate(ctf_data[ts]):
                ts_values[ts][n].extend(frame)
        alignment_data = self.get_ts_alignment_data()
        for ts in alignment_data:
            for n, frame in enumerate(alignment_data[ts]):
                ts_values[ts][n].extend(frame)
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
            if len(data[0]) == 7:
                tags.extend(["extra tags"])
            if len(data[0]) == 9:
                tags.extend(["extra tags"])

            ts_loop = ts_block.init_loop(
                prefix="_rln",
                tags=tags,
            )
            for line in data:
                ts_loop.add_row(line)
            sf_name = str(ts_dir / f"{ts_name}.star")
            ts_starfile.write_file(sf_name)

    # "CtfImage",
    # "DefocusU",
    # "DefocusV",
    # "CtfAstigmatism",
    # "DefocusAngle",
    # "CtfFigureOfMerit",
    # "CtfMaxResolution",
    # "CtfIceRingDensity",

    # # The nodetype for this in RELION should be TiltSeriesMoveGroupMetadata
    # # This will be updated in RELION/pipeliner at some point
    # def write_relion_tilt_series_master_file(self):
    #
    #     for name, frames in self.data.movie_stacks.items():
    #         # add to the main starfile
    #         import_data = self.main_import_data(name)
    #         main_loop.add_row(import_data)
    #
    #         # write the ts_starfile
    #         ts_starfile = cif.Document()
    #         ts_block = ts_starfile.add_new_block(name=name)
    #         ts_loop = ts_block.init_loop(
    #             prefix="_rln",
    #             tags=[
    #                 "MicrographMovieName",
    #                 "TomoTiltMovieFrameCount",
    #                 "TomoNominalStageTiltAngle",
    #                 "TomoNominalTiltAxisAngle",
    #                 "MicrographPreExposure",
    #                 "TomoNominalDefocus",
    #             ],
    #         )
    #         ts_loop.add_row(self.frame_import_data(name, frames))
    #         ts_starfile.write_file(import_data[0])
    #
    #     main_starfile.write_file("tilt_series.star")


# this will be used if the CETS data contains motioncorr information as if the CETS data
# was generated from a RELION motioncorr job
# there is currently not enough data in the CETS model to recreate RELION mocorr file
# def write_relion_mocorr_files(movie_frames: Dict[str, List[MovieFrame]]):
#     pass


# # this will be used if the CETS data contains ctf information as if the cets data was
# # generated from a RELION ctffind job
# def write_relion_ctf_files(movie_frames: Dict[str, List[MovieFrame]]):
#     main_starfile = cif.Document()
#     main_block = main_starfile.add_new_block(name="global")
#     main_loop = main_block.init_loop(
#         prefix="_rln",
#         tags=[
#             "TomoName",
#             "TomoTiltSeriesStarFile",
#             "Voltage",
#             "SphericalAberration",
#             "AmplitudeContrast",
#             "MicrographOriginalPixelSize",
#             "TomoHand",
#             "OpticsGroupName",
#         ],
#     )
#     ts_dir = Path("tilt_series")
#     ts_dir.mkdir(parents=True, exist_ok=True)
#     for name, frames in movie_frames.items():
#         # add to the main starfile
#         import_data = main_import_data(name, frames)
#         main_loop.add_row(import_data)
#
#         # write the ts_starfile
#         ts_starfile = cif.Document()
#         ts_block = ts_starfile.add_new_block(name=name)
#         ts_loop = ts_block.init_loop(
#             prefix="_rln",
#             tags=[
#                 "MicrographMovieName",
#                 "TomoTiltMovieFrameCount",
#                 "TomoNominalStageTiltAngle",
#                 "TomoNominalTiltAxisAngle",
#                 "MicrographPreExposure",
#                 "TomoNominalDefocus",
#                 "CtfImage",
#                 "DefocusU",
#                 "DefocusV",
#                 "CtfAstigmatism",
#                 "DefocusAngle",
#                 "CtfFigureOfMerit",
#                 "CtfMaxResolution",
#                 "CtfIceRingDensity",
#             ],
#         )
#         frame_groups = sort_frames(frames)
#         for frame_group, data in frame_groups.items():
#             basic_frame_data = frame_ctf_import_data(frame_group, data)
#
#         ts_starfile.write_file(import_data[0])
#
#     main_starfile.write_file("tilt_series.star")
