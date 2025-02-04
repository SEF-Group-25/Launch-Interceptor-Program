import pytest
import math
from src.utils import check_if_colinear, get_triangle_area, get_triangle_sides, calc_angle, get_length, get_quadrant, fits_in_circle

def test_get_length():

    # Normal cases
    assert get_length((2, 1), (3, 4)) == math.sqrt(10)
    assert get_length((-1, -2), (-7, 3)) == math.sqrt(61)
    assert get_length((0, 0), (1, 1)) == math.sqrt(2)

@pytest.mark.parametrize(
    "p1, p2, p3, epsilon, expected_result",
    [
        # Positive case: Points are collinear
        ((0, 0), (1, 1), (2, 2), 1e-6, True),

        # Negative case: Points are not collinear
        ((0, 0), (1, 1), (1, 2), 1e-6, False),

        # Nearly-collinear points
        ((0, 0), (1, 1), (1.00001, 1.00001), 1e-5, True),

        # Larger triangle
        ((0, 0), (100, 100), (200, 0), 1e-6, False),

    ]
)

def test_checkIfColinear(p1, p2, p3, epsilon, expected_result):
    result = check_if_colinear(p1, p2, p3, epsilon)
    assert result == expected_result

@pytest.mark.parametrize(
    "p1, p2, p3, expected_result",
    [
        # Positive case: Simple triangle
        ((0, 0), (3, 0), (0, 4), (3.0, 5.0, 4.0)),

        # Positive case: Points with negative coordinates
        ((-1, -1), (-4, -1), (-1, -5), (3.0, 5.0, 4.0)),

        # Positive case: Zero-length side (repeated points)
        ((0, 0), (0, 0), (3, 4), (0.0, 5.0, 5.0)),

        # Positive case: Large distances
        ((100, 100), (300, 100), (100, 500), (200.0, 447.21359549995793, 400.0)),
    ]
)

def test_get_triangle_sides(p1, p2, p3, expected_result):
    result = get_triangle_sides(p1, p2, p3)
    assert result == pytest.approx(expected_result)

@pytest.mark.parametrize(
    "p1, p2, p3, expected_result",
    [
        # Positive case: Right triangle
        ((0, 0), (4, 0), (0, 3), 6.0),

        # Edge case: Collinear points (area = 0)
        ((0, 0), (1, 1), (2, 2), 0.0),

        # Positive case: Isosceles triangle
        ((0, 0), (4, 0), (2, 4), 8.0),

        # Positive case: Points with negative coordinates
        ((-1, -1), (-4, -1), (-1, -5), 6.0),

        # Positive case: Large triangle
        ((0, 0), (1000, 0), (0, 2000), 1000000.0),
    ]
)

def test_get_triangle_area(p1, p2, p3, expected_result):
    result = get_triangle_area(p1, p2, p3)
    assert result == pytest.approx(expected_result)

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

@pytest.mark.parametrize(
    "x, y, expected_quadrant",
    [
        # Basic quadrants
        (1,  1, 1),   # Quadrant I
        (-1, 1, 2),    # Quadrant II
        (-2, -3, 3),   # Quadrant III
        ( 2, -5, 4),   # Quadrant IV

        (0,  0, 1),
        (0,  5, 1),
        (0, -2, 3),
        (3,  0, 1),
        (-4, 0, 2),
    ]
)
def test_get_quadrant(x, y, expected_quadrant):
    assert get_quadrant(x, y) == expected_quadrant

@pytest.mark.parametrize(
    "p1, p2, p3, radius, expected",
    [
        # Collinear: max distance is 4, half=2 => radius=2 fits exactly
        ((0,0), (2,0), (4,0), 2.0, True),

        # Collinear: max distance=4, half=2 => radius=1.9 => doesn't fit
        ((0,0), (2,0), (4,0), 1.9, False),

        # All points identical => trivially fits any radius >= 0
        ((1,1), (1,1), (1,1), 0.0, True),

        # Right triangle sides 3,4,5 => circumcircle radius=2.5
        # With radius=3 => fits
        ((0,0), (4,0), (0,3), 3.0, True),
    ]
)

def test_fits_in_circle(p1, p2, p3, radius, expected):
    if radius < 0:
        result = False  
    else:
        result = fits_in_circle(p1, p2, p3, radius)
    assert result == expected