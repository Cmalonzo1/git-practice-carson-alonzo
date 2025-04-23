#Buggy Code

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