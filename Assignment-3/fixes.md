# Documentation

### divide_numbers:

Initial Problem: This function did not handle dividing by zero

How the problem was discovered: Received ZeroDivisionError upon compilation

Fix: The function now throws a ValueError if there is an attempt to divide by zero

### reverse_string: 
Initial Problem: Did not properly handle non-string input

How the problem was discovered: Attempted to flip non-string input; received an error

Fix: The function now converts the input into a string before reversing it

### gen_list_element: 
Initial Problem: Did not check if the list was empty or if the inputted index was out of range

How the problem was discovered: Fed the function an empty list and a non-valid index

The function now checks the index after it's ensured the list is not empty and that the index is valid