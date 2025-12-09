from typing import List, Dict, Literal, Optional
import numpy as np
from scipy.spatial.transform import Rotation as R

IDENTITY2D = [[1, 0], [0, 1]]
IDENTITY3D = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def relion_eulers_to_matrix(rot: float, tilt: float, psi: float) -> List[List[int]]:
    """Convert the Euler angles from a RELION star file into a rotation matrix

    Args:
        tilt (float): _rlnAngleTilt (Phi)
        rot (float): _rlnAngleRot (Theta)
        psi (float): _rlnAnglePsi (Psi)

    Returns:
        np.ndarray: The transformation matrix

    """
    sipy_rot = R.from_euler(seq="zyz", angles=[rot, tilt, psi], degrees=True)
    matrix = sipy_rot.as_matrix().tolist()
    # tmp fix because affine is incorrectly typed, wants ints instead of floats
    return matrix


def affine_to_eulers(matrix: List[List[float]]) -> Dict[str, float]:
    """Convert an affine matrix to RELION Euler angles

    Args:
        matrix (List[List[float]]): affine transformation matrix
    Returns:
        Tuple[float, float, float]: euler angles tilt, rot, psi
    """
    affine = R.from_matrix(np.array(matrix))
    zyz_angles = affine.as_euler("zyz", degrees=True)
    return dict(zip(["rot", "tilt", "psi"], [float(x) for x in zyz_angles]))


def rotation_to_matrix_3d(
    rot_angle: float, axis: Literal["x", "y", "z"]
) -> List[List[float]]:
    """Convert rotation angle float into a rotation matrix
    Args:
        rot_angle (float): rotation angle
        axis (str): "x" or "y" or "z
    Returns:
        List[List[float]]: rotation matrix
    """
    matrix = R.from_euler(axis, rot_angle, degrees=True).as_matrix()
    return matrix.tolist()


def rotation_to_matrix_2d(rot_angle: float) -> List[List[float]]:
    """Convert clockwise rotation angle float into a rotation matrix
    Args:
        rot_angle (float): rotation angle
    Returns:
        List[List[float]]: rotation matrix
    """
    angle = np.deg2rad(rot_angle)
    c, s = np.cos(angle), np.sin(angle)
    return [[c, -s], [s, c]]


def matrix_2d_to_angle(matrix: List[List[float]]) -> float:
    """Convert a 2D rotation matrix to a rotation angle
    Args:
        matrix (List[List[float]]): 2D rotation matrix
    Returns:
        float: rotation angle
    """
    array = np.array(matrix)
    angle_rad = np.arctan2(array[1, 0], array[0, 0])
    return np.degrees(angle_rad)


def flip_matrix_2d(axes: Optional[List[str]] = None) -> List[List[int]]:
    """Generate a 2D flip matrix

    Args:
        axes (List[str]): axes to flip
    Returns:
        List[List[float]]: 2D flip matrix
    Raises:
        ValueError: If anything by 'x' or 'y' is given for axes
    """
    if not axes:
        return IDENTITY2D
    if any([x not in ("x", "y") for x in axes]):
        raise ValueError("axes must be 'x' or 'y'")
    x = -1 if "x" in axes else 1
    y = -1 if "y" in axes else 1
    return [[x, 0], [0, y]]


def flip_matrix_3d(axes: Optional[List[str]] = None) -> List[List[int]]:
    """Generate a 3D flip matrix

    Args:
        axes (List[str]): axes to flip
    Returns:
        List[List[float]]: 3D flip matrix
    Raises:
        ValueError: If anything by 'x', 'y', or 'z' is given for axes
    """
    if not axes:
        return IDENTITY3D
    if any([x not in ("x", "y", "z") for x in axes]):
        raise ValueError("axes must be 'x', 'y' or 'z'")
    x = -1 if "x" in axes else 1
    y = -1 if "y" in axes else 1
    z = -1 if "z" in axes else 1
    return [[x, 0, 0], [0, y, 0], [0, 0, z]]
