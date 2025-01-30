from LIC import *
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


PARAMETERS = {
    'LENGTH1': 10,
    'RADIUS1': 8,
    'PI': 3.141592653589793,
    'EPSILON': 10,
    'AREA1': 8,
    'Q_PTS': 0,
    'QUADS': 5,
    'N_PTS': 7,
    'DIST': 1,
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



def decide():
    # Setup
    PARAMETERS["POINTS"] = POINTS
    PARAMETERS["NUMPOINTS"] = NUMPOINTS
    functions = [LIC0, LIC1, LIC2, LIC3, LIC4, LIC5, LIC6, LIC7, LIC8, LIC9, LIC10, LIC11, LIC12, LIC13, LIC14]
    CMV = [False] * 15
    PUM = [[False] * 15 for _ in range(15)]
    FUV = [False] * 15

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
    PUM = calculate_pum(PUM, LCM, CMV)

    # Calculate FUV
    FUV = calculate_fuv(FUV, PUM)

    # Determines launch status.
    decision = determine_launch(FUV)

    # Prints "YES" or "NO" to standard output.
    print(decision)


def calculate_pum(PUM, LCM, CMV):
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


def calculate_fuv(FUV, PUM):
    for i in range(len(FUV)):
        if not PUV[i]:
            FUV[i] = True

        elif False not in PUM[i]:
            FUV[i] = True
    return FUV


def determine_launch(FUV):
    if all(FUV):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    decide()
