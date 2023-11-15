import pytest
from valid_anagram import is_anagram

test_cases = [
    ('anagram', 'nagaram', True),
    ('rat', 'car', False),
    ('anagram', 'anagram', True),
    ('anagram', 'abc', False)
]

@pytest.mark.parametrize("s, t, expected", test_cases)
def test_is_anagram(s, t, expected):
    assert is_anagram(s, t) == expected
