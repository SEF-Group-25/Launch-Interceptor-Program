import numpy as np
from src.utils import checkIfColinear, get_triangle_sides, get_triangle_area

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
