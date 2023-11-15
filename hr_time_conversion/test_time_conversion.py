import pytest
from time_conversion import time_conversion

test_cases = [
    { "s": '12:01:00PM', "expected": '12:01:00' },
    { "s": '07:05:45PM', "expected": '19:05:45' },
    { "s": '12:00:00AM', "expected": '00:00:00' },
    { "s": '12:00:00PM', "expected": '12:00:00' },
    { "s": '12:00:01AM', "expected": '00:00:01' },
    { "s": '01:00:00AM', "expected": '01:00:00' },
    { "s": '01:01:01PM', "expected": '13:01:01' },
]

@pytest.mark.parametrize("test_input", test_cases)
def test_time_conversion(test_input):
    s = test_input["s"]
    expected = test_input["expected"]
    assert time_conversion(s) == expected
