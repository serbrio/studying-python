#!/usr/bin/env python3
# Calculates 95 percentile of given in a file as argument list of values.


import sys
import math


def pcntl(s, p=95):
    items_in_p = math.ceil(p / (100/len(s)))
    print("items_in_p: {}".format(items_in_p))
    print("len of set: {}".format(len(s)))
    p_percentile_from_s = s[items_in_p - 1]
    return p_percentile_from_s


def percentile(arr, n):
# from https://stackoverflow.com/a/2753343
    k = (len(arr)-1) * n
    f = math.floor(k)
    c = math.ceil(k)
    if f==c:
        return arr[int(k)]
    d0 = arr[int(f)] * (c-k)
    d1 = arr[int(c)] * (k-f)
    return d0+d1


if __name__ == "__main__":
    array_file = sys.argv[1]
    s = set()
    with open(array_file) as f:
        for line in f:
            try:
                items = [int(item) for item in line.split()]
            except ValueError:
                items = [float(item) for item in line.split()]
            s.update(items)
    sorted_s = sorted(s)
    my_result = pcntl(sorted_s)
    acc_result = percentile(sorted_s, 0.95)
    print("My result: {}".format(my_result))
    print("Probably more accurate result: {}".format(acc_result))
