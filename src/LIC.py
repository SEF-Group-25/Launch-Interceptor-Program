from src.utils import calc_angle

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

def LIC5(POINTS):
    """
    Check if there exists a set of two consecutive points 
    (X[i], Y[i]) and (X[j], Y[j]) such that X[j] - X[i] < 0
    """

    for i in range(len(POINTS) - 1):
        if (POINTS[i+1][0] - POINTS[i][0] < 0):
            return True
    
    return False