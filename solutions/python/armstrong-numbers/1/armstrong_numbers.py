""" This module provides a function to check whether a number is an Armstrong number.
An Armstrong number equals the sum of its digits, each raised to the power of the total digit count.
Example: 153 = 1³ + 5³ + 3³ = 153
"""
def is_armstrong_number(number):
    """
    Check whether a number is an Armstrong number.

    Parameter:
        number (int): The number to check.

    Steps:
        1. Convert 'number' to a string to allow digit-by-digit iteration.
        2. Count the total digits, which determines the exponent power.
        3. Initialize 'total' to 0 as the accumulator.
        4. Loop each digit: convert back to int, raise to the power of digit count, add to 'total'.
        5. Return True if 'total' equals the original 'number', otherwise False.

    Example:
        >>> is_armstrong_number(153)
        True
        >>> is_armstrong_number(154)
        False
    """
    digits = str(number)
    number_length = len(digits)

    total = 0
    for member in digits:
        total += int(member) ** number_length

    return total == number
        
