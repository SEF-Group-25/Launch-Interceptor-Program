import pytest
from src.LIC import LIC1

@pytest.mark.parametrize(
    "POINTS, RADIUS1, expected_result",
    [
        # Positive case: There exists a triple that does NOT fit in the circle.
        ([(0, 0), (1, 1), (2, 2), (100, 100)], 1.0, True),

        # Negative case: All triples fit in the circle of radius RADIUS1.
        ([(0, 0), (1, 1), (2, 2), (3, 0)], 1.5, False),

        # Negative case: Points are repeated but still within circle.
        ([(0, 0), (0, 0), (1, 1), (1, 1)], 1.0, False),

        # Positive case: Collinear with large span and negative numbers, can't fit
        ([(-1, -1), (-2, -2), (100, 100)], 0.5, True),

        # Negative case: Collinear but still small enough to fit with negative numbers
        ([(-1, -1), (-2, -2), (-3, -3)], 2.0, False),
    ]
)

def test_LIC1(POINTS, RADIUS1, expected_result):
    result = LIC1(POINTS, RADIUS1)
    assert result == expected_result
