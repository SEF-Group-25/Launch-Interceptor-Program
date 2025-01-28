import pytest
from src.LIC import (
    LIC0,
    LIC1,
    LIC2,
    LIC3,
    LIC4,
    LIC5,
    LIC9,
    LIC12
)

@pytest.mark.parametrize(
    "POINTS, LENGTH1, expected_result",
    [
        # Positive case: There exists a 2 consecutive points that are further apart than LENGTH1.
        ([(0, 0), (1, 1), (2, 2), (3, 0)], 1.0, True),
        #negative case: All points are within LENGTH1
        ([(0, 0), (1, 1), (2, 2), (3, 0)], 4.0, False),
        #negative case: negative length
        ([(0, 0), (1, 1), (2, 2), (3, 0)], -1.0, False),
        
    ]
)

def test_LIC0(POINTS, LENGTH1, expected_result):
    result = LIC0(LENGTH1, POINTS )
    assert result == expected_result

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
    
    #create testcases for LIC3
@pytest.mark.parametrize(
    "AREA1, POINTS, expected_result",
    [
        # Positive case: Right triangle
        (1.0, [(0, 0), (4, 0), (0, 3)], True),

        # Negative case: All triangles have area less than AREA1.
        (10.0, [(0, 0), (1, 1), (2, 2), (3, 0)], False),

        # Negative case: area is 0.
        (1.0, [(0, 0), (1, 1), (2, 2), (3, 3)], False),

        
        # Negative case: Negative area
        (-1.0, [(0, 0), (4, 0), (0, 3)], False),
    ]
)

def test_LIC3(AREA1, POINTS, expected_result):
    result = LIC3(AREA1, POINTS)
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


@pytest.mark.parametrize(
    "POINTS, expected_result",
    [
        # Positive case. LIC5 is true if there exists X[j] - X[i] < 0, i = j - 1.
        ([(0, 0), (2.5, 3.6), (2.4, 8.09)], True),

        # Negative case. LIC5 is false if there doesn't exist X[j] - X[i] < 0, i = j - 1.
        ([(1.3, 2.5), (3.4, 5.5), (10, 0), (100.1, 3.3)], False)
    ]
)

def test_LIC5(POINTS, expected_result):
    result = LIC5(POINTS)
    assert result == expected_result


@pytest.mark.parametrize(
    "points, Q_PTS, QUADS, expected_result",
    [
        # Negatice case: Small Q_PTS, all points in one quadrant
        ([(1,1), (2,2), (3,3)], 2, 1, False),

        # Positice case: Two consecutive points in different quadrants
        ([(1,1), (-1,1)], 2, 1, True),

        # Positive case: Three consecutive points crossing 3 quadrants 
        ([(1,1), (-1,2), (0,-1), (1,-2)], 3, 2, True),

        # Negatice case: Invalid Q_PTS < 2
        ([(1,1), (2,2)], 1, 1, False),

        # Negatice case: Q_PTS > number of points
        ([(1,1), (2,2)], 3, 1, False),
    ]
)

def test_LIC4(points, Q_PTS, QUADS, expected_result):
    result = LIC4(points, Q_PTS, QUADS)
    assert result == expected_result
    

@pytest.mark.parametrize(
    "length1, length2, k_pts, points, expected_result",
    [
        # Positive case: distance between all pairs separeted  by K_PTS are larger than length1 and less than length2
        (1, 80, 1, [(0, 0), (1, 1), (2, 2), (3, 0)], True),

        # Negative case: distance between all pairs separeted  by K_PTS are more than or equal to length2
        (1, 2, 1, [(0, 0), (1, 1), (2, 2), (3, 0)], False),

        # Negative case: Negative length
        (-1, 80, 1, [(0, 0), (1, 1), (2, 2), (3, 0)], False),

        # Negative case: Negative length
        (1, -80, 1, [(0, 0), (1, 1), (2, 2), (3, 0)], False),
        
        # Negative case: Negative k_pts
        (1, 80, -1, [(0, 0), (1, 1), (2, 2), (3, 0)], False),
    ]
)

def test_LIC12(length1, length2, k_pts, points, expected_result):
    result = LIC12(length1, length2, k_pts, points)
    assert result == expected_result


