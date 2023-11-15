import pytest
from keys_and_rooms import keys_and_rooms

@pytest.mark.parametrize("rooms, expected", [
    ([[1], [1]], True),
    ([[1], [1], [1]], False),
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False)
])
def test_keys_and_rooms(rooms, expected):
    assert keys_and_rooms(rooms) == expected
