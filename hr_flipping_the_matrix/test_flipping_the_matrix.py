import pytest
from flipping_the_matrix import flipping_the_matrix

test_cases = [
    {
        "arr": [
            [1, 2],
            [3, 4],
        ],
        "expected": 4,
    },
    {
        "arr": [
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108]
        ],
        "expected": 414,
    },
]

@pytest.mark.parametrize("test_input", test_cases)
def test_flipping_the_matrix(test_input):
    matrix = test_input["arr"]
    expected = test_input["expected"]
    result = flipping_the_matrix(matrix)
    assert result == expected
