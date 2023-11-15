import pytest
from validate_password import validate, validate_orig

@pytest.mark.parametrize("password, expected", [
    ("Strongpwd9999#abc", []),
    ("Less10#", [1]),
    ("Password#", [1, 2]),
    ("#PassWord01111111222223x", [2, 3]),
    ("password#1111111", [2, 3, 4]),
    ("aaaapassword$$", [1, 2, 3, 4, 5]),
    ("LESS10#", [1, 4]),
    ("$sSSSt#passWord", [1, 2]),
    ("$sSSSt#passWordpassword", [2, 3])
])
def test_validate_password(password, expected):
    assert validate(password) == expected
    assert validate_orig(password) == expected
