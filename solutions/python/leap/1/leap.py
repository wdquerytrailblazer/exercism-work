"""
This module provides a function to determine whether a given year is a leap year.
A leap year occurs every 4 years, with exceptions for century years and exceptions to those exceptions.
"""

def leap_year(year):
    """
    Determine whether a given year is a leap year.

    Parameter:
        year (int): The year to check.

    Rules (ordered from most specific to least specific):
        "Most specific" means the rarest, narrowest condition that overrides broader rules.
        Always check the most specific exception first, or broader rules will swallow them.

        1. Divisible by 400 → IS a leap year.     (rarest, overrides rule 2)
        2. Divisible by 100 → NOT a leap year.    (overrides rule 3)
        3. Divisible by 4   → IS a leap year.     (general rule, checked last)
        4. Otherwise        → NOT a leap year.

    Why order matters:
        1900 is divisible by 4 AND 100.
        If we check rule 3 first, it returns True immediately and never reaches rule 2.
        Checking rule 2 first correctly returns False.

    Example:
        >>> leap_year(2000)
        True  # divisible by 400
        >>> leap_year(1900)
        False  # divisible by 100, but not 400
        >>> leap_year(2024)
        True  # divisible by 4, not a century year
        >>> leap_year(2023)
        False  # not divisible by 4
    """
    if year % 400 == 0:    # most specific: century years divisible by 400
        return True
    elif year % 100 == 0:  # less specific: century years not divisible by 400
        return False
    elif year % 4 == 0:    # least specific: general leap year rule
        return True
    else:
        return False
    
