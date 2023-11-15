import pytest
from reverse_string_in_words_3 import reverse_words

@pytest.mark.parametrize(
    "input_str, expected",
    [
        ('a', 'a'),
        ('Bill', 'lliB'),
        ('Bill was here!', 'lliB saw !ereh'),
        ('Let\'s take LeetCode contest', 's\'teL ekat edoCteeL tsetnoc'),
        ('God Ding', 'doG gniD')
    ]
)
def test_reverse_string_in_words_3(input_str, expected):
    assert reverse_words(input_str) == expected
