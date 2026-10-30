# To keep things standardized keeping all the names for transformations and
# systems as globals here rather than defining if the specific RELION file classes

# Base logical coordinate systems from CETS data model
BASE_LOGICAL_COORDS_2D = "logical coordinates 2d"
BASE_LOGICAL_COORDS_3D = "logical coordinates 3d"

# Align movie frame to projection
ALIGN_MOVIE_FRAME_XFROM = "align_movie_frame_to_projection"
ALIGN_MOVIE_FRAME_COORDS = "aligned_movie_frame"

# Align projection image to tomogram
ALIGN_PROJECTION_IMAGE_XFROM = "align_projection_image_to_tomogram"
ALIGN_PROJECTION_IMAGE_COORDS = "aligned_projection_image"

# Align subtomogram to tomogram R3D
ALIGN_SUBTOMOGRAM_XFROM = "align_subtomogram_to_tomogram"
ALIGN_SUBTOMOGRAM_COORDS = "aligned_subtomogram"

# Align map to tomogram
ALIGN_MAP_XFROM = "align_map_to_tomogram"
ALIGN_MAP_COORDS = "aligned_map"

# Align annotation to tomogram
ALIGN_ANNOTATION_XFROM = "align_annotation_to_tomogram"
ALIGN_ANNOTATION_COORDS = "aligned_annotation"

# set pixel size of image
IMAGE_PIXEL_SIZE_XFROM = "image_pixel_size"
IMAGE_PIXEL_SIZE_COORDS = "image_pixel_size"

# set super res pixel size of image
IMAGE_SUPER_RES_PIXEL_SIZE_XFROM = "image_pixel_size"
IMAGE_SUPER_RES_PIXEL_SIZE_COORDS = "image_pixel_size"

# gain reference
FLIP_GAIN_REF_XFORM = "flip_gain_reference"
FLIPPED_GAIN_REF_COORDS = "flipped_gain_reference"
GAIN_REF_ROTATION_XFORM = "gain_reference_rotation"
GAIN_REF_ALIGNMENT_SEQUENCE = "gain_reference_align_and_flip"
ALIGNED_GAIN_REF_COORDS = "gain_reference_aligned_and_flipped"
