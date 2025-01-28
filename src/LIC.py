import numpy as np
from src.utils import checkIfColinear, get_triangle_sides, get_triangle_area, calc_angle, get_length

def LIC0(length1, points):
    """
    Return true if there exists two consecutive points that 
    that are a distance greater than `length1` apart. otherwise False.
    """
    #make sure length1 is positive
    if length1 < 0:
        return False
    for i in range(len(points)-1):
        point_length = get_length(points[i], points[i+1])
        if point_length > length1:
            return True
    return False

def LIC1(points, radius1):
    """
    Returns True if there exists a set of three consecutive points 
    that CANNOT fit in a circle of radius `radius1`. Otherwise False.
    """
    n = len(points)
    for i in range(n - 2):
        p1, p2, p3 = points[i], points[i+1], points[i+2]

        if checkIfColinear(p1, p2, p3):
            a, b, c = get_triangle_sides(p1, p2, p3)
            diameter = np.max([a, b, c])  

            if diameter / 2.0 > radius1:
                return True
        else:
            area = get_triangle_area(p1, p2, p3)
            a, b, c = get_triangle_sides(p1, p2, p3)

            circumradius = (a * b * c) / (4.0 * area)
            if circumradius > radius1:
                return True 

    return False

def LIC2(POINTS, EPSILON):
    """
    Check if there exists a set of three consecutive points that 
    form an angle smaller than PI - EPSILON or greater than PI + EPSILON
    """

    PI = 3.1415926

    # boundary check
    if EPSILON < 0 or EPSILON >= PI:
        return False
    
    for i in range(len(POINTS) - 2):
        angle = calc_angle(POINTS[i], POINTS[i+1], POINTS[i+2])

        if angle == None:
            continue

        if angle < (PI - EPSILON):
            return True
    
    return False

# Write a function to check if there exists a set of
# three points separated by C_PTS and D_PTS that form 
# an angle smaller than PI - EPSILON or greater than PI + EPSILON
def LIC9(POINTS, EPSILON, C_PTS, D_PTS):
    
    if len(POINTS) < 5 or C_PTS < 1 or D_PTS < 1:
        return False
    if EPSILON < 0:
        return False
    
    PI = 3.1415926
    for i in range(len(POINTS) - C_PTS - D_PTS - 2):
        angle = calc_angle(POINTS[i], POINTS[i+C_PTS+1], POINTS[i+C_PTS+D_PTS+2])
        if angle == None:
            continue
        if angle < (PI - EPSILON) or angle > (PI + EPSILON):
            return True
    return False

def LIC5(POINTS):
    """
    Check if there exists a set of two consecutive points 
    (X[i], Y[i]) and (X[j], Y[j]) such that X[j] - X[i] < 0
    """

    for i in range(len(POINTS) - 1):
        if (POINTS[i+1][0] - POINTS[i][0] < 0):
            return True
    
    return False
