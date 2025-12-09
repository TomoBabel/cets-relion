from cets_relion.math_utils import (
    affine_to_eulers,
    relion_eulers_to_matrix,
    rotation_to_matrix_3d,
    rotation_to_matrix_2d,
    matrix_2d_to_angle,
)


def test_euler_to_matrix():
    # testing with values from first subtomo in TS_03
    rot, tilt, psi = (-1.40135, 97.396086, 4.337919)
    m = relion_eulers_to_matrix(rot, tilt, psi)
    assert m == [
        [-0.1264708962411244, -0.07875515190078805, 0.988839086228417],
        [-0.03411956457485091, 0.9965989433656185, 0.07500934205654208],
        [-0.9913833606215051, -0.024252260340359096, -0.12872785305128842],
    ]


def test_matrix_to_eulers():
    rtp = affine_to_eulers(
        [
            [-0.1264708962411244, -0.07875515190078805, 0.988839086228417],
            [-0.03411956457485091, 0.9965989433656185, 0.07500934205654208],
            [-0.9913833606215051, -0.024252260340359096, -0.12872785305128842],
        ]
    )
    print(rtp)
    assert round(rtp["rot"], 6) == -1.40135
    assert round(rtp["tilt"], 6) == 97.396086
    assert round(rtp["psi"], 6) == 4.337919


def test_rotation_to_matrix3d():
    r = rotation_to_matrix_3d(45, "x")
    assert r == [
        [1.0, 0.0, 0.0],
        [0.0, 0.7071067811865475, -0.7071067811865476],
        [0.0, 0.7071067811865476, 0.7071067811865475],
    ]
    r = rotation_to_matrix_3d(45, "y")
    assert r == [
        [0.7071067811865475, 0.0, 0.7071067811865476],
        [0.0, 1.0, 0.0],
        [-0.7071067811865476, 0.0, 0.7071067811865475],
    ]
    r = rotation_to_matrix_3d(45, "z")
    assert r == [
        [0.7071067811865475, -0.7071067811865476, 0.0],
        [0.7071067811865476, 0.7071067811865475, 0.0],
        [0.0, 0.0, 1.0],
    ]


def test_rotations_to_matrix_2d():
    r = rotation_to_matrix_2d(45)
    assert r == [
        [0.7071067811865476, -0.7071067811865475],
        [0.7071067811865475, 0.7071067811865476],
    ]


def test_matrix_to_angle_2d():
    r = [
        [0.7071067811865476, -0.7071067811865475],
        [0.7071067811865475, 0.7071067811865476],
    ]
    assert round(matrix_2d_to_angle(r), 6) == 45.0
