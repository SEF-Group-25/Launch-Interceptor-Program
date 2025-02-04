import pytest
from src.LIC import (
    LIC0,
    LIC1,
    LIC2,
    LIC3,
    LIC4,
    LIC5,
    LIC7,
    LIC6,
    LIC8,
    LIC9,
    LIC10,
    LIC11,
    LIC12,
    LIC13,
    LIC14

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
    #Type error test
def test_LIC0_invalid_input():
    with pytest.raises(TypeError):
        LIC0(1.0, 123)
        
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
    
#Test for LIC3
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
    #Type error test
def test_LIC3_invalid_input():
    with pytest.raises(TypeError):
        LIC3(True, 123)

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
    "POINTS, expected_result",
    [
        # Positive case. LIC5 is true if there exists X[j] - X[i] < 0, i = j - 1.
        ([(0, 0), (2.5, 3.6), (2.4, 8.09)], True),

        # Negative case. LIC5 is false if there doesn't exist X[j] - X[i] < 0, i = j - 1.
        ([(1.3, 2.5), (3.4, 5.5), (10, 0), (100.1, 3.3)], False),

        # Negative edge case. LIC5 is false if there doesn't exist X[j] - X[i] < 0, i = j - 1.
        # test X[j] == X[i]
        ([(0.0001, 0), (0.0001, 2), (1, -1)], False)
    ]
)
def test_LIC5(POINTS, expected_result):
    result = LIC5(POINTS)
    assert result == expected_result
    
#test LIC6
@pytest.mark.parametrize(
    "N_PTS, POINTS, DIST, expected_result",
    [
        # Positive case: straight line with one point 3 away
        (3, [(0, 0), (0, 3), (3, 0)], 2, True),

        # Negative case: straight line with one point less than 10 away
        (3, [(0, 0), (0, 9), (2, 0)], 10, False),

        # Negative case: N_PTS < 3
        (2, [(0, 0), (0, 3), (3, 0)], 1, False),

        # Negative case: Negative distance
        (3, [(0, 0), (0, 3), (3, 0)], -1, False),
        
        #Positive case: first and last point are the same
        (3, [(0, 0), (0, 3), (0, 0)], 2, True),
        
        #Negative case: first and last point are the same
        (3, [(0, 0), (0, 3), (0, 0)], 10, False),
    ]
)
def test_LIC6(N_PTS, POINTS, DIST, expected_result):
    result = LIC6(N_PTS, POINTS, DIST)
    assert result == expected_result
    #Type error test
def test_LIC6_invalid_input():
    with pytest.raises(TypeError):
        LIC6(3, True, 10)

@pytest.mark.parametrize(
    "POINTS, A_PTS, B_PTS, RADIUS1, expected_result",
    [
        # Positive case, There exists three points separated by exactly A_PTS and B_PTS points, 
        # cannot be contained within or on a circle of RADIUS1
        ([(0, 0), (1.2, 2.3), (4, 0), (0, 1), (0, 3)], 1, 1, 2.4, True),

        # Positive case, three points are collinear but still cannot be contained.
        ([(0, 0), (1.2, 2.3), (4, 0), (0, 1), (5.5, 0)], 1, 1, 2.4, True),

        # Negative case, There doesn't exist three points cannot be contained.
        ([(0, 0), (1.2, 2.3), (4, 0), (0, 1), (0, 3)], 1, 1, 2.6, False),

        # Negative case, the parameter is not valid.
        ([(0, 0), (1.2, 2.3), (4, 0), (0, 1), (0, 3)], 2, 1, 2.4, False),
    ]
)
def test_LIC8(POINTS, A_PTS, B_PTS, RADIUS1, expected_result):
    result = LIC8(POINTS, A_PTS, B_PTS, RADIUS1)
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
#Type error test
def test_LIC9_invalid_input():
    with pytest.raises(TypeError):
        LIC9(True, 0.1, 1, 1)

@pytest.mark.parametrize(
    "POINTS, G_PTS, expected_result",
    [
        # Positive case, There exists a set of two points 
        # separated by G_PTS consecutive points such that X[j] - X[i] < 0.
        ([(0, 1), (2.5, 6.6), (1.1, 1), (-0.1, 3)], 2, True),

        # Negative case, There doesn't exist such two points.
        ([(0, 1), (4.5, 4.5), (1, 2), (5, 5)], 1, False),

        # Negative case, parameter is not valid.
        ([(0, 1), (2.5, 6.6), (1.1, 1), (-0.1, 3)], 3, False),
    ]
)
def test_LIC11(POINTS, G_PTS, expected_result):
    result = LIC11(POINTS, G_PTS)
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
    #Type error test
def test_LIC12_invalid_input():
    with pytest.raises(TypeError):
        LIC12(1, 80, 1, True)

@pytest.mark.parametrize(
    "POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result",
    [
        # Positive case, there exist three data points, separated by exactly E_PTS and F_PTS intervening points, 
        # that form a triangle with an area greater than AREA1. There also exists such three points, 
        # form a triangle with an area less than AREA2.
        ([(0, 0), (0.1, 0.2), (3, 4), (4, 0), (1, 2), (0, 3)], 2, 1, 5, 6.05, True),

        # Negative case, there doesn't exists such points satisfiying area requirements.
        ([(1, 1), (0, 0), (2.5, 2.5), (3, 1), (10, 10.1), (2, 5)], 1, 1, 1, 0, False),

        # Negative case, parameter is not valid.
        ([(0, 0), (0.1, 0.2), (3, 4), (4, 0), (1, 2), (0, 3)], 2, 2, 5, 6.05, False),

        # Negative case, AREA2 is not valid.
        ([(0, 0), (0.1, 0.2), (3, 4), (4, 0), (1, 2), (0, 3)], 2, 2, 5, -1, False),
    ]
)
def test_LIC14(POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result):
    result = LIC14(POINTS, E_PTS, F_PTS, AREA1, AREA2)
    assert result == expected_result

@pytest.mark.parametrize(
    "points, K_PTS, LENGTH1, expected",
    [
        # Negative case: fewer than 3 points
        ([(0,0), (1,1)], 1, 1.0, False),

        # Positice case: Exactly 3 points
        ([(0,0), (1,1), (2,2)], 1, 2.0, True),

        # Negative case: 4 points, multiple possible pairs, but none exceed LENGTH1=4
        ([(0,0), (1,1), (2,2), (3,3)], 1, 4.0, False),

        # Positive case: 4 points, check a bigger gap 
        ([(0,0), (1,1), (2,2), (3,3)], 2, 4.0, True),

        # Positive case: Negative coordinates, multiple pairs. 
        ([(-1, -1), (0,0), (5,5), (6,6)], 1, 3.0, True),

        # Negative case: K_PTS is out of valid range
        ([(0,0), (1,1), (2,2), (3,3)], 10, 2.0, False),
    ]
)

def test_LIC7(points, K_PTS, LENGTH1, expected):
    result = LIC7(points, K_PTS, LENGTH1)
    assert result == expected

@pytest.mark.parametrize(
    "POINTS, E_PTS, F_PTS, AREA1, expected_result",
    [
        # Negative case: Fewer than 5 points 
        ([(0,0), (1,0), (2,0), (3,0)], 1, 1, 1.0, False),

        # Positive case: Exactly 5 points, forms a large triangle
        ([(0,0), (10,10), (10,0), (5,5), (0,10)], 1, 1, 2.0, True),

        # Negative case: Multiple points, but no triple has area > 10.0
        ([(0,0), (1,0), (2,0), (3,0), (4,0), (5,0)], 1, 1, 10.0, False),

        # Positive case: At least one triple is large enough (area > 5.0)
        ([(0,0), (1,1), (2,6), (3,3), (0,10), (5,5)], 1, 1, 5.0, True),

        # Negative case: Valid spacing, but all triangles have area <= 10.0
        ([(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)], 2, 1, 10.0, False),
    ]
)
    
def test_LIC10(POINTS, E_PTS, F_PTS, AREA1, expected_result):
    result = LIC10(POINTS, E_PTS, F_PTS, AREA1)
    assert result == expected_result

@pytest.mark.parametrize(
    "POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result",
    [
        # Negative case: Fewer than 5 points 
        ([(0,0), (1,1), (2,2), (3,3)], 1, 1, 2.0, 5.0, False),

        # Positive case: 
        # There's a triple that doesn't fit in radius=2.0 
        # AND there's a triple that fits in radius=5.0
        ([(0,0), (1,1), (4,0), (2,2), (0,3)], 1, 1, 2.0, 5.0, True),

        # Negative case: We find a triple that doesn't fit in RADIUS1 but 
        # no triple fits in RADIUS2
        ([(0,0), (4,4), (8,8), (12,12), (1,1)], 1, 1, 3.0, 2.5, False),

        # Negative case: We find a triple that fits in RADIUS2, but 
        # none that fails RADIUS1
        ([(0,0), (1,1), (2,2), (3,3), (4,4)], 1, 1, 10.0, 10.0, False),
    ]
)

def test_LIC13(POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result):
    result = LIC13(POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
    assert result == expected_result