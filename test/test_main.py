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
    "PUM, case, expected_result",
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

                "c",

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
        "c",

                [False, True, False, True, False] * 3
        ),
    ]
)
def test_calculate_fuv(PUM, case, expected_result):
    result = calculate_fuv(PUM, case)
    assert result == expected_result


@pytest.mark.parametrize(
    "PUM, case",
    [
        # Test the too long PUM errors out.
        (
                [["*", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, "toolong"]],
                "c",

        ),
    ]
)
def test_calculate_fuv_index_error(PUM, case):
    with pytest.raises(IndexError):
        calculate_fuv(PUM, case)



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
    "case, expected_result",
    [
        (
                "a",

                "NO\n",
        ),

        (
                "b",

                "YES\n",
        ),

        (
                "ab",

                "NO\n",
        ),
    ]
)
def test_decide(capsys, case, expected_result):
    decide(case)
    captured = capsys.readouterr()

    assert captured.out == expected_result