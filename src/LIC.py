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