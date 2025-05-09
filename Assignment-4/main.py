def expensive_op(n):
    """Multiply input number by sum of first 1000 integers.

    Args:
        n (int): Input multiplier

    Returns:
        int: Result of n * sum(range(1000))
    """
    return n * sum(range(1000))

def slow_func(lst):
    """Generate list of results from expensive_op for each index.

    Args:
        lst (list): Input list determining the range length

    Returns:
        list: List of expensive_op results for indices 0 to len(lst)-1
    """
    return [expensive_op(i) for i in range(len(lst))]

def main():
    """Execute the main program flow.

    Creates a list of first 1000 integers, processes it through slow_func,
    and prints the results.
    """
    numbers = list(range(1000))
    print(slow_func(numbers))
    print("Done")

if __name__ == "__main__":
    main()