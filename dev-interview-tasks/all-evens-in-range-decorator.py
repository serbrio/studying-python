#!/usr/bin/env python3
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(n):
        n *= -1
        return func(n)
    return wrapper


@my_decorator
def evens(n: int) -> list:
    """Return a list with all even numbers in the range from 0 to n.
    """
    
    if n < 0:
        return [ x for x in range(0, n, -1) if x % 2 == 0 ]
    elif n == 0:
        return [0]
    else:
        return [ x for x in range(n) if x % 2 == 0 ]


def test():
    assert evens(8) == [0, -2, -4, -6], f'Returned: {evens(8)}'
    assert evens(1) == [0], f'Returned: {evens(1)}'
    assert evens(-5) == [0, 2, 4], f'Returned: {evens(-5)}'
    assert evens(-4) == [0, 2], f'Returned: {evens(-4)}'
    assert evens(0) == [0], f'Returned: {evens(0)}'


test()
