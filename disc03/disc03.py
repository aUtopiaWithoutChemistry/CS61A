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


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    # the parameter for recursive call should be the variable 
    # number, but not like n in this case
    if n == 2:
        return True
    @trace1
    def f(i):
        if n % i == 0:
            return False
        elif i < (n / 2):
            return f(i + 1)
        else:
            return True
    return f(2)


def trace1(fn):
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced


def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

# using even and odd function to count how many times they
# have been called
def even(n):
    return 1 + hailstone(n // 2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if n != 1:
        return 1 + hailstone(n * 3 + 1)
    else:
        return 1
