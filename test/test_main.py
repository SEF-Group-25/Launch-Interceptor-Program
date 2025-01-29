import pytest
from src.main import *


@pytest.mark.parametrize(
    "PUM, LCM, CMV, expected_result",
    # Example from the paper.
    [
        ([[False] * 5 for _ in range(5)],

         [["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"],
          ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED"],
          ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED"],
          ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED"],
          ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"]],

         [False, True, True, True, False],

         [["*", False, True, False, True],
          [False, "*", True, True, True],
          [True, True, "*", True, True],
          [False, True, True, "*", True],
          [True, True, True, True, "*"]]
         ),
    ]
)
def test_calculate_pum(PUM, LCM, CMV, expected_result):
    result = calculate_pum(PUM, LCM, CMV)
    assert result == expected_result


@pytest.mark.parametrize(
    "FUV, PUM, expected_result",
    # Example from the paper.
    [
        (
         [False, False, False, False, False],

         [["*", False, True, False, True],
          [False, "*", True, True, True],
          [True, True, "*", True, True],
          [False, True, True, "*", True],
          [True, True, True, True, "*"]],

        [False, True, True, True, True]
         ),
    ]
)
def test_calculate_fuv(FUV, PUM, expected_result):
    result = calculate_fuv(FUV, PUM)
    assert result == expected_result


@pytest.mark.parametrize(
    "FUV, expected_result",
    # Example from the paper.
    [
        (
         [False, True, True, True, True],

         "NO",
         ),
    ]
)
def test_determine_launch(FUV, expected_result):
    result = determine_launch(FUV)
    assert result == expected_result