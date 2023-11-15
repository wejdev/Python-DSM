import pytest
from rotting_oranges import rotting_oranges, rotting_oranges_queue

@pytest.mark.parametrize("grid, expected", [
    (
        [
            [0, 2]
        ],
        0
    ),
    (
        [
            [0, 1]
        ],
        -1
        ),
    (
        [
            [1, 1]
        ],
        -1
    ),
    (
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ],
        4
    ),
    (
        [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ],
        -1
     ),
    (
        [
            [2, 0, 0, 2],
            [1, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 0]
        ],
        3
    ),
    (
        [
            [2, 0, 0, 2],
            [1, 1, 1, 1],
            [0, 0, 1, 1],
            [1, 0, 0, 0]
        ],
        -1
    ),
])
def test_rotting_oranges(grid, expected):
    # assert rotting_oranges(grid) == expected TODO: fix this
    assert rotting_oranges_queue(grid) == expected
