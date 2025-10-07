import argparse
from typing import List
from pathlib import Path
from cets_data_model.models.models import (
    Region,
    Dataset,
    MovieStackCollection,
    MovieStackSeries,
    TiltSeries,
    Tomogram,
    ParticleMap,
)

from cets_relion.main_converter import RelionCetsConverter


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="RELION-CETS C")
    parser.add_argument(
        "--job",
        "-j",
        required=True,
        help="The job in the RELION project to get data from",
    )
    parser.add_argument(
        "--tomos",
        "-t",
        nargs="+",
        required=False,
        help="Tomograms to operate on. If empty, all tomos will be used",
    )
    parser.add_argument(
        "--region_name",
        "-r",
        required=False,
        help="Name to give the Region in the CETS data",
        default=None,
    )
    parser.add_argument(
        "--dataset_name",
        "-d",
        required=False,
        help="Name to give the Dataset in the CETS data",
        default=None,
    )

    parser.add_argument(
        "--output_name",
        "-o",
        required=False,
        default="relion_to_cets.json",
    )

    return parser.parse_args(argv)


def get_raw_movies(
    con: RelionCetsConverter, tomo_name: str
) -> List[MovieStackCollection]:
    movies = []
    for movie_set in con.movies:
        movies.append(movie_set.make_movie_cets_for_tilt_series(tomo_name))
    clean_movies: List[MovieStackSeries] = [x for x in movies if x is not None]
    if movies:
        mov_stack_col = MovieStackCollection(
            gain_file=con.find_gain_file(tomo_name),
            defect_file=con.find_defect_file(tomo_name),
            movie_stacks=clean_movies,
        )
        return [mov_stack_col]
    else:
        return []


def get_tilt_series(con: RelionCetsConverter, tomo_name: str) -> List[TiltSeries]:
    all_tilt_series = []
    # see if there is a tilt series entry in the converter

    for con_ts in con.tilt_series:
        all_tilt_series.extend(con_ts.get_cets_projection_images(tomo_name))

    # if not try to use the ctf entry
    if not all_tilt_series:
        for con_ctf in con.ctf:
            all_tilt_series.extend(con_ctf.get_cets_projection_images(tomo_name))

    # if not finally try the motioncorr entry
    if not all_tilt_series:
        for con_mocorr in con.mocorr:
            all_tilt_series.extend(con_mocorr.get_cets_projection_images(tomo_name))

    return all_tilt_series


def get_tomos(con: RelionCetsConverter, tomo_name: str) -> List[Tomogram]:
    tomos = []
    for tomofile in con.tomos:
        cets_tomo = tomofile.get_cets_tomo(tomo_name)
        if cets_tomo is not None:
            tomos.append(tomofile)
    return tomos


# ToDo: Fix output type annotation when model has proper sphere object
def get_coord_annotations(con: RelionCetsConverter, tomo_name: str) -> list:
    annotations = []
    for coord_set in con.picks:
        annotations.append(coord_set.get_tomo_cets_coords_set(tomo_name))
        coords_sec = coord_set.get_secondary_annotations(tomo_name)
        if coords_sec is not None:
            annotations.extend(coords_sec.get_cets())
    return annotations


def get_particles(con, tomo_name: str) -> List[ParticleMap]:
    parts = []
    for part_set in con.particles:
        parts.append(part_set.get_cets_particles(tomo_name))
    return parts


def main(argv=None):
    args = parse_args(argv)
    con = RelionCetsConverter(args.job)
    dataset = Dataset(name=args.dataset_name, regions=[])
    # make a region for each tomogram
    tomos = args.tomos
    if not tomos:
        tomos = con.get_all_tomo_names()

    for tomo_name in tomos:
        # ToDo: Region needs a name field
        region = Region(
            movie_stack_collections=[], tomograms=[], tilt_series=[], annotations=[]
        )
        region.movie_stack_collections = get_raw_movies(con, tomo_name)
        region.tilt_series = get_tilt_series(con, tomo_name)
        region.tomograms = get_tomos(con, tomo_name)
        region.annotations = get_coord_annotations(con, tomo_name)

        dataset.regions.append(region)
    outname = args.output_name
    outname = outname + ".json" if not Path(outname).suffix == ".json" else outname
    with open(outname, "w") as out:
        out.write(dataset.model_dump_json(indent=2))


if __name__ == "__main__":
    main()  # uses sys.argv automatically
