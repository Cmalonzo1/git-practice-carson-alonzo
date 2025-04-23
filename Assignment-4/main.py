import math
import random


def expensive_op(n):
    total = 0
    for i in range(1000):
        total += i * n
    return total


def slow_func(lst):
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result


def unused_function():
    x = 10
    y = 20
    z = x + y
    return z


def main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")


if __name__ == "__main__":
    main()