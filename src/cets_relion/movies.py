from typing import List, Optional
from gemmi import cif
from src.cets_relion.relion_reader import RelionPipeline
from src.models.models import MovieStack, MovieFrame, MovieStackSeries, CTFMetadata
from src.cets_relion.utils import get_image_dims
from src.cets_relion.ctf import RelionCtfStarFile


class RelionMoviesStarFile(object):
    """An object for handling the data from a tilt_series.star file output from a
    relion.importtomo job.  This file contains info about the raw tomographic tilt
    series movies

    Attrs:
        pipeline (RelionPipeline): A graph representation of the pipeline
        movies_file (str): The path of the tilt_series.star file containing data about
            the movies
        ctf_files (List[str]): A list of files that provide information about the CTF
            of the movies. These should be the global results files from CtfFind jobs

    """

    def __init__(
        self,
        movies_file: str,
        pipeline: str = "default_pipeline.star",
        ctf_files: Optional[List[str]] = None,
    ) -> None:
        """Instantiate a RelionMoviesStarFile

        Args:
            movies_file (str): The path of the tilt_series.star file containing data about
            the movies
        pipeline (str): Relative path to the pipeline file. Almost always
            default_pipeline.star
        ctf_files (Optional[List[str]]): A list of paths to files that provide information about
            the CTF of the movies.  If the object is being instantiated starting at the
            movies file this will be automatically determined and should be None.  If
            the object is being created whilst tracing backward from a downstream file
            this should be provided to make sure the correct ctf jobs are used.

        """
        self.pipeline = RelionPipeline(pipeline)
        self.movies_file = movies_file
        if ctf_files is None:
            ctf_files = self.pipeline.next_downstream_file_of_type(
                start=movies_file, relion_type="TomogramGroupMetadata", kwds=["ctffind"]
            )
        self.ctf_files: List[str] = ctf_files

    def get_tilt_movies_starfile(self, ts_name: str):
        """Get the starfile that contains info about movies for a specific tilt series

        Args:
            ts_name (str): The name of the tilt series

        Returns:
            str: Path to the tilt series metadata file
        """
        ciffile = cif.read_file(self.movies_file)
        global_block = ciffile.find_block("global")
        files = global_block.find(
            prefix="_rln", tags=["TomoName", "TomoTiltSeriesStarFile"]
        )
        ts_file = [x[1] for x in files if x[0] == ts_name]
        if not ts_file:
            return ts_file
        else:
            # there will only ever be one ts starfile associated with a ts name
            return ts_file[0]

    def make_movie_cets_for_tilt_series(self, ts_name: str):
        """Get a CETS object for the movies associated with a specific tilt series

        Args:
            ts_name (str): The name of the tilt series
        """
        # a list to hold the movies for this tilt series
        movie_stacks: List[MovieStack] = []

        # get the data from the starfile
        movies_starfile = self.get_tilt_movies_starfile(ts_name)
        ciffle = cif.read_file(movies_starfile)
        cifdata = ciffle.sole_block().find(
            prefix="_rln",
            tags=[
                "MicrographMovieName",
                "TomoTiltMovieFrameCount",
                "TomoNominalStageTiltAngle",
                "TomoNominalTiltAxisAngle",
                "MicrographPreExposure",
                "TomoNominalDefocus",
            ],
        )
        # process each movie
        for row_n, row in enumerate(cifdata):
            movie_name = row[0]
            width, height = get_image_dims(movie_name)[:2]

            # find the ctf data for this move - applies for all frames
            cets_ctf: Optional[CTFMetadata] = None
            for f in self.ctf_files:
                cets_ctf = RelionCtfStarFile(f).get_tilt_image_ctf(movie_name)
                if cets_ctf:
                    break

            # make a MovieFrame for each frame in the movie
            frames: List[MovieFrame] = []
            # calculate the frame dosages
            try:
                dose = float(cifdata[row_n + 1][4]) - float(cifdata[row_n][4])
            # the last frames expose rate is assumed to be the same as previous
            except IndexError:
                dose = float(cifdata[row_n][4]) - float(cifdata[row_n - 1][4])

            for n in range(int(row[1])):
                frame_n = f"{n + 1:05}"
                frame_dose = dose * (float(n + 1) / float(row[1]))
                frames.append(
                    MovieFrame(
                        path=f"{frame_n}@{movie_name}",
                        section=str(n),
                        nominal_tilt_angle=float(row[2]),
                        accumulated_dose=frame_dose + float(row[4]),
                        ctf_metadata=cets_ctf,
                        width=width,
                        height=height,
                    )
                )

            # make a MovieStack for the movie
            movie_stacks.append(MovieStack(images=frames, path=movie_name))

        # return a CETS MovieStackSeries for the tilt series
        return MovieStackSeries(stacks=movie_stacks)

    def get_all_movies_stack_series(self):
        """Get CETS MovieStackSeries for every tilt series in the file

        Returns:
            List[MovieStackSeries]: MovieStackSeries for every tilt series in the file
        """
        all_tilt_series = (
            cif.read_file(self.movies_file)
            .sole_block()
            .find(prefix="_rln", tags=["TomoName"])
        )
        return [self.make_movie_cets_for_tilt_series(x[0]) for x in all_tilt_series]
