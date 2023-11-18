import pytest
from teleporter import destinations, destinations_orig, destinations_orig_2, destinations_2, destinations_orig_ugly

teleporters_1 = ["3,1", "4,2", "5,10"]
teleporters_2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
teleporters_3 = ["6,18", "36,26", "41,21", "49,55", "54,52", "71,58", "74,77", "78,76", "80,73", "92,85"]
teleporters_4 = ["97,93", "99,81", "36,33", "92,59", "17,3", "82,75", "4,1", "84,79", "54,4", "88,53", "91,37", "60,57", "61,7", "62,51", "31,19"]
teleporters_5 = ["3,8", "8,9", "9,3"]

@pytest.mark.parametrize("teleporter, die_sides, start_pos, last_square, expected", [
    (teleporters_1, 6, 0, 20 ,[1, 2, 10, 6]),
    (teleporters_2, 6, 46, 100 ,[48, 49, 50, 51, 52, 29]),
    (teleporters_2, 10, 0, 50 ,[1, 2, 3, 4, 7, 8, 9, 10, 22]),
    (teleporters_3, 10, 95, 100 ,[96, 97, 98, 99, 100]),
    (teleporters_3, 10, 70, 100 ,[72, 73, 75, 76, 77, 79, 58]),
    (teleporters_4, 6, 0, 100 ,[1, 2, 3, 5, 6]),
    (teleporters_5, 6, 0, 20 ,[1, 2, 4, 5, 6, 8]),
])
def test_teleporter(teleporter, die_sides, start_pos, last_square, expected):
    assert sorted(destinations(teleporter, die_sides, start_pos, last_square)) == sorted(expected)
    assert sorted(destinations_orig(teleporter, die_sides, start_pos, last_square)) == sorted(expected)
    assert sorted(destinations_orig_2(teleporter, die_sides, start_pos, last_square)) == sorted(expected)
    assert sorted(destinations_2(teleporter, die_sides, start_pos, last_square)) == sorted(expected)
    assert sorted(destinations_orig_ugly(teleporter, die_sides, start_pos, last_square)) == sorted(expected)
