import pytest
from src.main import *

NUMPOINTS_valid = 50

POINTS_valid = [(24, 1), (41, 27), (50, 17), (27, 10), (17, 29), (24, 21), (3, 22), (19, 35),
 (11, 18), (15, 3), (24, 36), (6, 43), (50, 28), (35, 39), (13, 48), (16, 13),
 (12, 21), (26, 48), (6, 1), (38, 20), (2, 6), (6, 16), (15, 14), (41, 48),
 (9, 4), (42, 40), (5, 11), (8, 9), (50, 25), (26, 9), (41, 39), (29, 49),
 (21, 33), (32, 5), (41, 26), (15, 5), (10, 10), (50, 5), (13, 10), (11, 25),
 (40, 36), (26, 11), (48, 17), (2, 1), (1, 21), (10, 34), (43, 43), (5, 9),
 (15, 19), (24, 19)]

LCM_valid = [
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

PUV_valid = [True, False, True, False, True, True, False, True, False, True, True, False, True, False, True]

PARAMETERS_valid = {
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

@pytest.mark.parametrize(
    "LCM, CMV, expected_result",
    [
        # ALl true.
        (
         [["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"] * 3,
          ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED"] * 3,
          ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED"] * 3,
          ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED"] * 3,
          ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"] * 3] * 3,

         [True, True, True, True, True] * 3,

         [["*", True, True, True, True, True, True, True, True, True, True, True, True, True, True],
          [True, "*", True, True, True, True, True, True, True, True, True, True, True, True, True],
          [True, True, "*", True, True, True, True, True, True, True, True, True, True, True, True],
          [True, True, True, "*", True, True, True, True, True, True, True, True, True, True, True],
          [True, True, True, True, "*", True, True, True, True, True, True, True, True, True, True],
          [True, True, True, True, True, "*", True, True, True, True, True, True, True, True, True],
          [True, True, True, True, True, True, "*", True, True, True, True, True, True, True, True],
          [True, True, True, True, True, True, True, "*", True, True, True, True, True, True, True],
          [True, True, True, True, True, True, True, True, "*", True, True, True, True, True, True],
          [True, True, True, True, True, True, True, True, True, "*", True, True, True, True, True],
          [True, True, True, True, True, True, True, True, True, True, "*", True, True, True, True],
          [True, True, True, True, True, True, True, True, True, True, True, "*", True, True, True],
          [True, True, True, True, True, True, True, True, True, True, True, True, "*", True, True],
          [True, True, True, True, True, True, True, True, True, True, True, True, True, "*", True],
          [True, True, True, True, True, True, True, True, True, True, True, True, True, True, "*"]]
         ),

        # NOTUSED works.
        (
         [["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"] * 3,
          ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"] * 3,
          ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"] * 3,
          ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"] * 3,
          ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"] * 3] * 3,

         [False, False, False, False, False] * 3,

         [["*", True, True, True, True, True, True, True, True, True, True, True, True, True, True],
          [True, "*", True, True, True, True, True, True, True, True, True, True, True, True, True],
          [True, True, "*", True, True, True, True, True, True, True, True, True, True, True, True],
          [True, True, True, "*", True, True, True, True, True, True, True, True, True, True, True],
          [True, True, True, True, "*", True, True, True, True, True, True, True, True, True, True],
          [True, True, True, True, True, "*", True, True, True, True, True, True, True, True, True],
          [True, True, True, True, True, True, "*", True, True, True, True, True, True, True, True],
          [True, True, True, True, True, True, True, "*", True, True, True, True, True, True, True],
          [True, True, True, True, True, True, True, True, "*", True, True, True, True, True, True],
          [True, True, True, True, True, True, True, True, True, "*", True, True, True, True, True],
          [True, True, True, True, True, True, True, True, True, True, "*", True, True, True, True],
          [True, True, True, True, True, True, True, True, True, True, True, "*", True, True, True],
          [True, True, True, True, True, True, True, True, True, True, True, True, "*", True, True],
          [True, True, True, True, True, True, True, True, True, True, True, True, True, "*", True],
          [True, True, True, True, True, True, True, True, True, True, True, True, True, True, "*"]]
         ),
    ]
)
def test_calculate_pum(LCM, CMV, expected_result):
    result = calculate_pum(LCM, CMV)
    assert result == expected_result


@pytest.mark.parametrize(
    "LCM, CMV",
    [
        # Test the too long PUM errors out.
        (
                [["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"] * 3,
                 ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED"] * 3,
                 ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED"] * 3,
                 ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED"] * 3,
                 ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"] * 3] * 3,

                [False] * 12
        ),
    ]
)
def test_calculate_pum_index_error(LCM, CMV):
    with pytest.raises(IndexError):
        calculate_pum(LCM, CMV)


@pytest.mark.parametrize(
    "PUM, PUV, expected_result",
    [
        # All true.
        (
                [["*", True, True, True, True, True, True, True, True, True, True, True, True, True, True],
                 [True, "*", True, True, True, True, True, True, True, True, True, True, True, True, True],
                 [True, True, "*", True, True, True, True, True, True, True, True, True, True, True, True],
                 [True, True, True, "*", True, True, True, True, True, True, True, True, True, True, True],
                 [True, True, True, True, "*", True, True, True, True, True, True, True, True, True, True],
                 [True, True, True, True, True, "*", True, True, True, True, True, True, True, True, True],
                 [True, True, True, True, True, True, "*", True, True, True, True, True, True, True, True],
                 [True, True, True, True, True, True, True, "*", True, True, True, True, True, True, True],
                 [True, True, True, True, True, True, True, True, "*", True, True, True, True, True, True],
                 [True, True, True, True, True, True, True, True, True, "*", True, True, True, True, True],
                 [True, True, True, True, True, True, True, True, True, True, "*", True, True, True, True],
                 [True, True, True, True, True, True, True, True, True, True, True, "*", True, True, True],
                 [True, True, True, True, True, True, True, True, True, True, True, True, "*", True, True],
                 [True, True, True, True, True, True, True, True, True, True, True, True, True, "*", True],
                 [True, True, True, True, True, True, True, True, True, True, True, True, True, True, "*"]],
                [True, False, True, False, True, True, False, True, False, True, True, False, True, False, True],

                [True, True, True, True, True] * 3
        ),

        # All false leads to some true due to PUV.
        (
        [
        ["*", False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, "*", False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, "*", False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, "*", False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, "*", False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, "*", False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, "*", False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, "*", False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, "*", False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, "*", False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, "*", False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, "*", False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, "*", False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, "*", False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, "*"]
        ],
        [True, False, True, False, True, True, False, True, False, True, True, False, True, False, True],

                [False, True, False, True, False] * 3
        ),
    ]
)
def test_calculate_fuv(PUM, PUV, expected_result):
    result = calculate_fuv(PUM, PUV)
    assert result == expected_result


@pytest.mark.parametrize(
    "PUM, PUV",
    [
        # Test the too long PUM errors out.
        (
                [["*", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, "toolong"]],
                [True, False, True, False, True, True, False, True, False, True, True, False, True, False, True]

        ),
    ]
)
def test_calculate_fuv_index_error(PUM, PUV):
    with pytest.raises(IndexError):
        calculate_fuv(PUM, PUV)



@pytest.mark.parametrize(
    "FUV, expected_result",
    [
        # Failing example from the paper.
        (
                [False, True, True, True, True] * 3,

                "NO",
        ),

        # Passing test.
        (
                [True, True, True, True, True] * 3,

                "YES",
        ),

        # Empty array.
        (
                [],

                "NO",
        ),
    ]
)
def test_determine_launch(FUV, expected_result):
    result = determine_launch(FUV)
    assert result == expected_result

@pytest.mark.parametrize(
    "NUMPOINTS, POINTS, PARAMETERS, LCM, PUV, expected_output",
    [
        # Valid input, but not launched
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, LCM_valid, PUV_valid, "NO\n"),

        # Invalid NUMPOINTS, 2 <= NUMPOINTS <= 100
        (1, POINTS_valid, PARAMETERS_valid, LCM_valid, PUV_valid, "Invalid NUMPOINTS\n"),

        # Invalid NUMPOINTS, 2 <= NUMPOINTS <= 100
        (101, POINTS_valid, PARAMETERS_valid, LCM_valid, PUV_valid, "Invalid NUMPOINTS\n"),

        # Invalid NUMPOINTS, NUMPOINT is an integer
        (1.1, POINTS_valid, PARAMETERS_valid, LCM_valid, PUV_valid, "Invalid NUMPOINTS\n"),

        # Invalid POINTS, inconsistent with NUMPOINTS
        (2, [(0, 0)], PARAMETERS_valid, LCM_valid, PUV_valid, "Invalid POINTS\n"),

        # Invalid POINTS, wrong type
        (2, (0, 0), PARAMETERS_valid, LCM_valid, PUV_valid, "Invalid POINTS\n"),

        # Invalid POINTS, wrong type
        (2, [(0, 0), (0, 1, 2)], PARAMETERS_valid, LCM_valid, PUV_valid, "Invalid point in POINTS\n"),

        # Invalid POINTS, wrong type
        (2, [(0, 0), (0, "1")], PARAMETERS_valid, LCM_valid, PUV_valid, "Invalid coordinates in POINTS\n"),

        # Invalid PARAMETERS, we assume it as a dict
        (NUMPOINTS_valid, POINTS_valid, list(PARAMETERS_valid.items()), LCM_valid, PUV_valid, "Invalid PARAMETERS\n"),

        # Invalid PARAMETERS, missing parameter
        (NUMPOINTS_valid, POINTS_valid, {k: v for k, v in PARAMETERS_valid.items() if k != "DIST"}, LCM_valid, PUV_valid, "Missing parameter: DIST\n"),
        
        # Invalid PARAMETERS, parameter is invalid
        (NUMPOINTS_valid, POINTS_valid, {k: (v if k != "QUADS" else 1.5) for k, v in PARAMETERS_valid.items()}, LCM_valid, PUV_valid, "Invalid parameter: QUADS\n"),

        # Invalid LCM, not a list
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, tuple(LCM_valid), PUV_valid, "Invalid LCM\n"),

        # Invalid LCM, wrong size
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, LCM_valid[:-1], PUV_valid, "Invalid LCM\n"),

        # Invalid LCM, wrong size
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, [x[:-1] for x in LCM_valid], PUV_valid, "Invalid LCM\n"),

        # Invalid LCM, invalid element LCM[0][0] is ANDDD
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, 
        [
            ["ANDDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"],
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
        ], PUV_valid, "Invalid element in LCM\n"),

        # Invalid LCM, invalid element LCM[0][1] != LCM[1][0]
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, 
        [
            ["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"],
            ["ORR", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ORR", "NOTUSED"],
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
        ], PUV_valid, "LCM not symmetric\n"),

        # Invalid PUV, not a list
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, LCM_valid, tuple(PUV_valid), "Invalid PUV\n"),
        
        # Invalid PUV, wrong size
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, LCM_valid, PUV_valid[:-1], "Invalid PUV\n"),

        # Invalid PUV, element not a bool
        (NUMPOINTS_valid, POINTS_valid, PARAMETERS_valid, LCM_valid, 
         [2, False, True, False, True, True, False, True, False, True, True, False, True, False, True], 
         "Invalid element in PUV\n"),
    ]
)
def test_decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV, expected_output, capsys):
    decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV)
    captured = capsys.readouterr()
    assert captured.out == expected_output