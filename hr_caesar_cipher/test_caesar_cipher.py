import pytest
from caesar_cipher import caesar_cipher

@pytest.mark.parametrize("input_str, k, expected", [
    ("", 0, ""),
    ("abc", 1, "bcd"),
    ("xyz", 2, "zab"),
    ("ABC", 1, "BCD"),
    ("XYZ", 2, "ZAB"),
    ("Hello, World!", 3, "Khoor, Zruog!"),
    ("Khoor, Zruog!", -3, "Hello, World!"),
    # Add more test cases as needed
])
def test_caesar_cipher(input_str, k, expected):
    result = caesar_cipher(input_str, k)
    assert result == expected
