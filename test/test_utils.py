import pytest
import math
from src.utils import calc_angle

def test_calc_angle():

    # Normal cases
    assert math.isclose(calc_angle((1, 0), (0, 0), (0, 1)), math.pi / 2, rel_tol=1e-6)
    assert math.isclose(calc_angle((1, 0), (0, 0), (1, 0)), 0, rel_tol=1e-6)
    assert math.isclose(calc_angle((1, 0), (0, 0), (-1, 0)), math.pi, rel_tol=1e-6)

    # Special cases: One of the points coincides with the vertex
    assert calc_angle((0, 0), (0, 0), (1, 1)) is None
    assert calc_angle((1.5, 1.5), (1.5, 1.5), (1.5, 1.5)) is None

    # Edge cases
    assert math.isclose(calc_angle((1e9, 0), (0, 0), (0, 1e9)), math.pi / 2, rel_tol=1e-6)
    assert math.isclose(calc_angle((1e-6, 0), (0, 0), (0, 1e-6)), math.pi / 2, rel_tol=1e-6)

    # collinear points
    assert math.isclose(calc_angle((2, 0), (1, 0), (0, 0)), math.pi, rel_tol=1e-9)