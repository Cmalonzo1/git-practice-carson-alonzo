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


"""
Buggy Code

def divide_numbers(a, b):
     result = a / b  # Bug: No handling for division by zero
    return round(result, 2)


def reverse_string(s):
    reversed_s = s[::-1]  # Bug: Might not handle non-string input properly
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case


def get_list_element(lst, index):
        if index < len(lst):  # Bug: Incorrect boundary check
        return lst[index]
    else:
        return "Not found"  # Bug: Should probably raise an exception instead
 
"""