import math
import numpy as np

def get_length(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x ** 2 + y ** 2)

def check_if_colinear(p1, p2, p3, epsilon=1e-6):
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

def calc_angle(end1, vertex, end2):
    """
    Calculates the angle formed by three points, with the second point as the vertex.

    Parameters:
    - end1, vertex, end2: Three points represented as (x, y) tuples.

    Returns:
    - The angle in radians (range [0, PI]).
    - Returns None if the angle is undefined.
    """

    vec1 = (end1[0] - vertex[0], end1[1] - vertex[1])
    vec2 = (end2[0] - vertex[0], end2[1] - vertex[1])

    norm_vec1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
    norm_vec2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)

    # first point or the last point (or both) coincides with the vertex
    if norm_vec1 == 0 or norm_vec2 == 0:
        return None
    
    cos_angle = vec1[0] * vec2[0] + vec1[1] * vec2[1]

    # account for floating-point errors
    cos_angle = max(-1, min(1, cos_angle))

    angle = math.acos(cos_angle)

    return angle

def get_quadrant(x, y):
    """
    Return the quadrant number of a point (x, y), 
    using the priority I > II > III > IV for axis points.

    Quadrant labeling:
      I:  x >= 0, y >= 0
      II: x < 0,  y >= 0
      III: x <= 0, y < 0
      IV: x > 0,  y < 0
    """
    if x > 0:
        if y >= 0:
            return 1
        else:
            return 4
    elif x < 0:
        if y >= 0:
            return 2
        else:
            return 3
    else:  # x == 0
        if y > 0:
            return 1
        elif y < 0:
            return 3
        else: 
            return 1
        
def fits_in_circle(p1, p2, p3, radius):
    """
    Returns True if the three points (p1, p2, p3) can be enclosed by 
    a circle of the given radius, False otherwise.

    Uses:
      - check_if_colinear(p1, p2, p3)
      - get_length(p1, p2)
      - get_triangle_sides(p1, p2, p3)
      - get_triangle_area(p1, p2, p3)
    """
    if check_if_colinear(p1, p2, p3):
        #print("collinear")
        d12 = get_length(p1, p2)
        d23 = get_length(p2, p3)
        d13 = get_length(p1, p3)
        max_dist = max(d12, d23, d13)
        return (max_dist / 2.0) <= radius
    else:
        #print("not collinear")
        a, b, c = get_triangle_sides(p1, p2, p3)
        area = get_triangle_area(p1, p2, p3)

        R = (a * b * c) / (4.0 * area)
        return R <= radius
