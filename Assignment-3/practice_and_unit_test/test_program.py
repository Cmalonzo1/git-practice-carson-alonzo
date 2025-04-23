import pytest

from program import divide_numbers, reverse_string, get_list_element

@pytest.mark.parametrize("a,b,expected, exception",[
(10,2, 5, None), #whole number
(1,5, 0.2, None), #floats
# negatives
(-10, 2, -5, None),
(-10, -2, 5, None),

#by zero
    (10,0, None, ValueError)
])

def test_divide_numbers(a, b, expected, exception):
    if exception:
        with pytest.raises(exception):
            divide_numbers(a, b)
    else:
        assert divide_numbers(a, b) == expected

@pytest.mark.parametrize("input_str, expected_output", [
    ("Hello", "OLLEh"),
    ("Python3", "3NOHTYp"),
    ("", ""),  # Empty string
    ("a", "A"),  # Single character
    ("ABC", "cba"),  # All uppercase
    ("abc", "CBA"),  # All lowercase
    ("PyThOn", "NoHtYp"),  # Mixed case
    ("1234!", "!4321"),  # Numbers & special characters
])
def test_reverse_string(input_str, expected_output):
    assert reverse_string(input_str) == expected_output


@pytest.mark.parametrize("lst, index, expected_exception, expected_message", [
    ([10, 20, 30], 1, None, None),  # Valid case
    ([10, 20, 30], 5, IndexError, "Index out of range"),  # Out-of-range index
    ([10, 20, 30], -1, None, None),  # Negative index
    (([]), 1, ValueError, "Empty List"), # Empty List
    ([10, 20, 30], 3, IndexError, "Index out of range")  # Boundary case
])
def test_get_list_element(lst, index, expected_exception, expected_message):
    if expected_exception:
        with pytest.raises(expected_exception, match=expected_message):
            get_list_element(lst, index)
    else:
        assert get_list_element(lst, index) == lst[index]






