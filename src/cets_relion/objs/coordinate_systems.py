from cets_data_model.models.models import CoordinateSystem, Axis

x_axis_logical = Axis(name="logical coordinates x axis", axis_unit="pixel/voxel")
y_axis_logical = Axis(name="logical coordinates y axis", axis_unit="pixel/voxel")
z_axis_logical = Axis(name="logical coordinates z axis", axis_unit="pixel/voxel")

x_axis_physical = Axis(name="physical coordinates x axis", axis_unit="Ångstrom")
y_axis_physical = Axis(name="physical coordinates y axis", axis_unit="Ångstrom")
z_axis_physical = Axis(name="physical coordinates z axis", axis_unit="Ångstrom")

# RELION's logical coordinate system. 0,0,0 is at the bottom left corner
RELION_COORDS_LOGICAL = CoordinateSystem(
    name="logical coordinates", axes=[x_axis_logical, y_axis_logical, z_axis_logical]
)

# RELION's physical coordinate system. 0,0,0 is at the centre
RELION_COORDS_PHYSICAL = CoordinateSystem(
    name="physical coordinates",
    axes=[x_axis_physical, y_axis_physical, z_axis_physical],
)


def physical_coords(name: str) -> CoordinateSystem:
    coords = RELION_COORDS_PHYSICAL.model_copy()
    coords.name = name
    return coords


def logical_coords(name: str) -> CoordinateSystem:
    coords = RELION_COORDS_LOGICAL.model_copy()
    coords.name = name
    return coords
