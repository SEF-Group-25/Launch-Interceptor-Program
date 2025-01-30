import pytest
from src.main import *


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


def test_decide(capsys):
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

    decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV)
    captured = capsys.readouterr()

    assert captured.out == "NO\n"