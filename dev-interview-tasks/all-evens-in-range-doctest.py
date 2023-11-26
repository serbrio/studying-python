#!/usr/bin/env python3


def evens(n: int) -> list:
    """Return a list with all even numbers in the range from 0 to n.
    
    >>> evens(8)
    [0, 2, 4, 6]

    >>> evens(1)
    [0]

    >>> evens(-5)
    [0, -2, -4]
    
    >>> evens(-4)
    [0, -2]

    >>> evens(0)
    [0]

    """
    
    if n < 0:
        return [ x for x in range(0, n, -1) if x % 2 == 0 ]
    elif n == 0:
        return [0]
    else:
        return [ x for x in range(n) if x % 2 == 0 ]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
