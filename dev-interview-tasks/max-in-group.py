#!/usr/bin/env python3
#
# Task:
# Given a list of random integers and some number k;
# 1) For every group of k integers in the list 
# (window of k integers beginning with the first one in the list,
# then with beginning with the second one etc) find the max number;
# 2) Return list of all found max numbers.


def maximums_in_group(array, k):
    """Return the list of max numbers in every group of k numbers
    in the given array.

    >>> maximums_in_group([8, 4, 3, 9, 2, 0, 1], 3)
    [8, 9, 9, 9, 2]
    >>> maximums_in_group([1, 6, 3], 4)
    [6]
    >>> maximums_in_group([], 2)
    []
    >>> maximums_in_group([99, 34, 2], 3)
    [99]
    >>> maximums_in_group([-23, -111, 34, 0, 4], 4)
    [34, 34]
    """

    length = len(array)

    if length == 0:
        return []
    elif length <= k:
        return [max(array)]

    maximums = []
    counter = 0

    while counter + k <= length:
        group = [ array[i] for i in range(counter, counter + k) ]
        maximums.append(max(group))
        counter +=1
    return  maximums


if __name__ == "__main__":
    import doctest
    doctest.testmod()
