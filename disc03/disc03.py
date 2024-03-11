def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        # due to the shape of expected output is in triangular 
        # shape, and we can't keep the number on each digit after
        # divided by 10, so we should call swipe again in the same
        # level to get the forward part.
        swipe(n % 10)
        swipe(n // 10)
        swipe(n % 10)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    # base case
    if n < 3:
        return n
    else:
        return n * skip_factorial(n - 2)
