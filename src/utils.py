import numpy as np

def checkIfColinear(p1, p2, p3, epsilon=1e-6):
    """
    Check if three points are collinear.
    """
    area = abs(p1[0] * (p2[1] - p3[1]) + 
               p2[0] * (p3[1] - p1[1]) + 
               p3[0] * (p1[1] - p2[1]))
    return area < epsilon

def get_triangle_sides(p1, p2, p3):
    """
    Calculate the lengths of the sides of a triangle.
    """
    p1, p2, p3 = np.array(p1), np.array(p2), np.array(p3)
    a = np.linalg.norm(p2 - p1)  
    b = np.linalg.norm(p3 - p2)  
    c = np.linalg.norm(p1 - p3)  
    return a, b, c

def get_triangle_area(p1, p2, p3):
    """
    Calculate the area of a triangle given three points.

    Parameters:
        p1, p2, p3 (tuple): Points as (x, y).

    Returns:
        float: Area of the triangle.
    """
    matrix = np.array([
        [p1[0], p1[1], 1],
        [p2[0], p2[1], 1],
        [p3[0], p3[1], 1]
    ])
    return 0.5 * abs(np.linalg.det(matrix))
