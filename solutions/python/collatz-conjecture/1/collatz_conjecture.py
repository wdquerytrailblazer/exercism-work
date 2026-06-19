def steps(number):
    """
    Count how many steps it takes to reach 1 using the Collatz conjecture.

    Steps:
        1. Raise an error if number is not a positive integer.
        2. Initialize a step counter to 0.
        3. Loop until number reaches 1:
            - If even: divide by 2.
            - If odd: multiply by 3 and add 1.
            - Increment step counter each iteration.
        4. Return the total step count.

    Example:
        >>> steps(12)
        9
        >>> steps(1)
        0
    """
    if number <= 0: 
        raise ValueError("Only positive integers are allowed")

    count=0
    while number != 1:
        if number%2==0:
            number = number//2
        else:
            number = number * 3 + 1
        count += 1

    return count
        
