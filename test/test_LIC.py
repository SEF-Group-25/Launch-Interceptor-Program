import pytest
from src.LIC import (
    LIC2, LIC9
)

@pytest.mark.parametrize(
    "POINTS, EPSILON, expected_result",
    [
        # Positive case.
        ([(0, 0), (1, 1), (2, 2), (3, 0)], 0.1, True), 

        # Negative case 1, no angle is smaller than (PI - EPSILON).
        ([(0, 0), (1.2, 1.2), (2, 2), (4.5, 4.5)], 0.1, False), 

        # Negative case 2, point[0] coincides with point[1]
        ([(0, 0), (0, 0), (1, 1), (3, 0)], 0.1, False),

        # Negative case 3, EPSILON < 0
        ([(0, 0), (1, 1), (2, 2), (3, 0)], -0.1, False),
    ]
)
def test_LIC2(POINTS, EPSILON, expected_result):
    result = LIC2(POINTS, EPSILON)
    assert result == expected_result
    
@pytest.mark.parametrize(
    "POINTS, EPSILON, C_PTS, D_PTS, expected_result",
    [
        # Positive case.
        ([(0, 0), (1, 1), (2, 2), (3, 0), (4, 0)], 0.1, 1, 1, True), 

        # Positive case 1, no angle is smaller than (PI - EPSILON).
        ([(0, 0), (1.2, 1.2), (2, 2), (4.5, 4.5), (5, 0)], 0.1, 1, 1, False), 

        # Negative case 2, point[0] coincides with point[1]
        ([(0, 0), (0, 0), (1, 1), (3, 0), (4, 0)], 0.1, 1, 1, False),

        # Negative case 3, EPSILON < 0
        ([(0, 0), (1, 1), (2, 2), (3, 0), (4, 0)], -0.1, 1, 1, False),

        # Negative case 4, C_PTS < 1
        ([(0, 0), (1, 1), (2, 2), (3, 0), (4, 0)], 0.1, 0, 1, False),

        # Negative case 5, D_PTS < 1
        ([(0, 0), (1, 1), (2, 2), (3, 0), (4, 0)], 0.1, 1, 0, False),
    ]
    
    
    
)
    
def test_LIC9(POINTS, EPSILON, C_PTS, D_PTS, expected_result):
    result = LIC9(POINTS, EPSILON, C_PTS, D_PTS)
    assert result == expected_result