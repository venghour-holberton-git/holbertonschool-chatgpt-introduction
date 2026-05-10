#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Calculates the factorial of a number.

    Parameters:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the given number.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
