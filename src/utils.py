import math

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

