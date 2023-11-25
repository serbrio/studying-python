#!/usr/bin/env python3
#
# Task: 
# Given sorted list of integers (positive and negative). 
# 1) Produce a new list of raised integers to the power of 2,
# 2) return sorted list.
# *) Additionally: explore doctest while solving the task.


def sort_powers(integers_list, power):
    """Return the sorted list of powers of integers
    given in the integers_list.

    >>> sort_powers([1, 2, 3], 2)
    [1, 4, 9]
    >>> sort_powers([], 3)
    []
    >>> sort_powers([-5, 1, 2, 3], 2)
    [1, 4, 9, 25]
    >>> sort_powers([-2, -1, 1, 2, 3], 3)
    [-8, -1, 1, 8, 27]
    >>> sort_powers(['a'], 2)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    >>> sort_powers(2, 2)
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable
    """

    powers =  [ i ** power for i in integers_list ]
    return sorted(powers)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
