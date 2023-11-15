import pytest
from flood_fill import flood_fill

@pytest.mark.parametrize("image, sr, sc, new_color, expected", [
    (
        [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ],
        1, 1, 2,
        [
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1]
        ]
    ),
    (
        [
            [0, 0, 0],
            [0, 0, 0]
        ],
        0, 0, 2,
        [
            [2, 2, 2],
            [2, 2, 2]
        ]
    )
])
def test_flood_fill(image, sr, sc, new_color, expected):
    result = flood_fill(image, sr, sc, new_color)
    assert result == expected
