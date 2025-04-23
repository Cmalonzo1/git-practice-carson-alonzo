def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    if b == 0:
        raise ValueError("Cannot divide by 0")
    else:
        result = a / b  # Bug: No handling for division by zero

    return round(result, 2)


def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    reversed_s = str(s[::-1])  # Converts the given text into a string
    flipped_case = ''.join(char.swapcase() for char in reversed_s)  # Flip case
    return flipped_case


def get_list_element(lst, index):
    if not lst:
        raise ValueError("Empty List")

    if -len(lst) <= index >= len(lst):
        raise IndexError("Index out of range")
    else:
        return lst[index]


