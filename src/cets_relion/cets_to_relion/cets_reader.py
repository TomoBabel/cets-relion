from typing import Union, Dict, List
from pathlib import Path
import json
from itertools import chain

from cets_data_model.models.models import Dataset, MovieFrame, ProjectionImage, Tomogram


class CetsReader(object):
    """An object for reding CETS data"""

    def __init__(self, cets_dataset_path: Union[str, Path]):
        """INstantiate a CETS reader
        Args:
            cets_dataset_path (Union[str, Path]): Path to the CETS data in json format
        """

        with open(cets_dataset_path) as f:
            data = json.load(f)
        self.data = Dataset.model_validate(data)
        regions = self.data.regions
        movie_collections = list(
            chain.from_iterable([x.movie_stack_collections for x in regions])
        )
        movie_stacks_dict = {}
        for mov_stack_collection in movie_collections:
            for mov in mov_stack_collection.movie_stacks:
                movie_stacks_dict[mov.name] = mov.stacks
        self.movie_stacks: Dict[str, List[MovieFrame]] = movie_stacks_dict

        all_tilt_series = list(chain.from_iterable([x.tilt_series for x in regions]))
        tilt_image_dict = {}
        for tilt_series in all_tilt_series:
            tilt_image_dict[tilt_series.name] = tilt_series.images
        self.tilt_angle_images: Dict[str, List[ProjectionImage]] = tilt_image_dict

        all_tomos = list(chain.from_iterable([x.tomograms for x in regions]))
        all_tomograms: Dict[str, Tomogram] = {}
        for tomo in all_tomos:
            all_tomograms[tomo.path] = tomo
        self.tomograms = all_tomograms
        self.averages = self.data.averages
