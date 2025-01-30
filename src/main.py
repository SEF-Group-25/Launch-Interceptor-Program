from src.LIC import *
import inspect

NUMPOINTS = 50

POINTS = [(24, 1), (41, 27), (50, 17), (27, 10), (17, 29), (24, 21), (3, 22), (19, 35),
 (11, 18), (15, 3), (24, 36), (6, 43), (50, 28), (35, 39), (13, 48), (16, 13),
 (12, 21), (26, 48), (6, 1), (38, 20), (2, 6), (6, 16), (15, 14), (41, 48),
 (9, 4), (42, 40), (5, 11), (8, 9), (50, 25), (26, 9), (41, 39), (29, 49),
 (21, 33), (32, 5), (41, 26), (15, 5), (10, 10), (50, 5), (13, 10), (11, 25),
 (40, 36), (26, 11), (48, 17), (2, 1), (1, 21), (10, 34), (43, 43), (5, 9),
 (15, 19), (24, 19)]


LCM = [
    ["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"],
    ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED"],
    ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "ORR", "ORR", "ANDD", "ANDD", "NOTUSED"],
    ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "ANDD", "NOTUSED"],
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
    ["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"],
    ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED"],
    ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "ORR", "ORR", "ANDD", "ANDD", "NOTUSED"],
    ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "ANDD", "NOTUSED"],
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
    ["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"],
    ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED"],
    ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "ORR", "ORR", "ANDD", "ANDD", "NOTUSED"],
    ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "ANDD", "NOTUSED"],
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"]
]


PUV = [True, False, True, False, True, True, False, True, False, True, True, False, True, False, True]

PI = 3.1415926535

PARAMETERS = {
    'LENGTH1': 10,
    'RADIUS1': 8,
    'EPSILON': 10,
    'AREA1': 8,
    'Q_PTS': 0,
    'QUADS': 5,
    'DIST': 1,
    'N_PTS': 7,
    'K_PTS': 4,
    'A_PTS': 7,
    'B_PTS': 0,
    'C_PTS': 5,
    'D_PTS': 6,
    'E_PTS': 9,
    'F_PTS': 9,
    'G_PTS': 4,
    'LENGTH2': 3,
    'RADIUS2': 3,
    'AREA2': 2
}



def decide(
        NUMPOINTS,
        POINTS,
        PARAMETERS,
        LCM,
        PUV
):
    # Type check
    if not isinstance(NUMPOINTS, int) or not (2 <= NUMPOINTS <= 100):
        print("Invalid NUMPOINTS")
        return
    
    if not isinstance(POINTS, list) or len(POINTS) != NUMPOINTS:
        print("Invalid POINTS")
        return

    for point in POINTS:
        if not isinstance(point, tuple) or len(point) != 2:
            print("Invalid point in POINTS")
            return
        x, y = point
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            print("Invalid coordinates in POINTS")
            return
    
    if not isinstance(PARAMETERS, dict):
        print("Invalid PARAMETERS")
        return
    
    required_params = {
        "LENGTH1": (float, int),
        "RADIUS1": (float, int),
        "EPSILON": (float, int),
        "AREA1": (float, int),
        "Q_PTS": int,
        "QUADS": int,
        "DIST": (float, int),
        "N_PTS": int,
        "K_PTS": int,
        "A_PTS": int,
        "B_PTS": int,
        "C_PTS": int,
        "D_PTS": int,
        "E_PTS": int,
        "F_PTS": int,
        "G_PTS": int,
        "LENGTH2": (float, int),
        "RADIUS2": (float, int),
        "AREA2": (float, int),
    }

    for param, expected_type in required_params.items():
        if param not in PARAMETERS:
            print("Missing parameter: {}".format(param))
            return
        
        param_value = PARAMETERS[param]
        if not isinstance(param_value, expected_type):
            print("Invalid parameter: {}".format(param))
            return

    if not isinstance(LCM, list) or len(LCM) != 15 or not all(len(row) == 15 for row in LCM):
        print("Invalid LCM")
        return
    
    valid_values_LCM = {"ANDD", "ORR", "NOTUSED"}
    for i in range(15):
        for j in range(15):
            if LCM[i][j] not in valid_values_LCM:
                print("Invalid element in LCM")
                return
            if LCM[i][j] != LCM[j][i]:
                print("LCM not symmetric")
                return
    
    if not isinstance(PUV, list) or len(PUV) != 15:
        print("Invalid PUV")
        return

    for value in PUV:
        if not isinstance(value, bool):
            print("Invalid element in PUV")
            return

    # Setup
    PARAMETERS["POINTS"] = POINTS
    PARAMETERS["NUMPOINTS"] = NUMPOINTS
    functions = [LIC0, LIC1, LIC2, LIC3, LIC4, LIC5, LIC6, LIC7, LIC8, LIC9, LIC10, LIC11, LIC12, LIC13, LIC14]
    CMV = [False] * 15

    # Gather CMV
    for i in range(len(CMV)):
        func = functions[i]

        # Get function's parameter names
        sig = inspect.signature(func)
        param_names = sig.parameters.keys()

        # Filter PARAMETERS to include only required arguments
        valid_args = {k: v for k, v in PARAMETERS.items() if k in param_names}

        # Call function with filtered arguments
        if func(**valid_args):
            CMV[i] = True

    # Calculate PUM
    PUM = calculate_pum(LCM, CMV)

    # Calculate FUV
    FUV = calculate_fuv(PUM, PUV)

    # Determines launch status.
    decision = determine_launch(FUV)

    # Prints "YES" or "NO" to standard output.
    print(decision)


def calculate_pum(LCM, CMV):
    PUM = [[False] * 15 for _ in range(15)]
    for i in range(len(PUM)):
        for j in range(len(PUM[0])):
            if LCM[i][j] == "NOTUSED":
                PUM[i][j] = True

            if LCM[i][j] == "ANDD" and (CMV[i] and CMV[j]):
                PUM[i][j] = True

            if LCM[i][j] == "ORR" and (CMV[i] or CMV[j]):
                PUM[i][j] = True

            if i == j:
                PUM[i][j] = "*"
    return PUM


def calculate_fuv(PUM, PUV):
    FUV = [False] * 15
    for i in range(len(FUV)):
        if not PUV[i]:
            FUV[i] = True

        elif False not in PUM[i]:
            FUV[i] = True
    return FUV


def determine_launch(FUV):
    if all(FUV) and len(FUV) != 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV)
