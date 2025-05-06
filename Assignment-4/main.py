"""
import math
import random

"""

"""
Unoptimized function
def expensive_op(n):
    total = 0
    for i in range(1000):
        total += i * n
    return total
"""

#updated function
@profile
def expensive_op(n):
    return n * sum(range(1000))

@profile
def slow_func(lst):
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result

"""
Unused function
def unused_function():
    x = 10
    y = 20
    z = x + y
    return z
"""


def main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")


if __name__ == "__main__":
    main()