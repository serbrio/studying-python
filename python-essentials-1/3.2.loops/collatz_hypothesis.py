#!/usr/bin/env python3
"""Lothar Collatz hypothesis (1937):
Take any non-negative and non-zero integer number n;
1) if it's even, evaluate a new n as n ÷ 2;
2) otherwise, if it's odd, evaluate a new n as 3 × n + 1;
3) if n ≠ 1, go back to step 1.
The hypothesis says that regardless of the initial value of n, it will always go to 1.
"""


def check_collatz_hypothesis(n):
    """Take non-negative and non-zero integer number;
    1) if it's even, evaluate a new n as n ÷ 2;
    2) otherwise, if it's odd, evaluate a new n as 3 × n + 1;
    3) if n ≠ 1, go back to step 1.
    Counts and prints overall steps done till n became 1.
    Prints every intermediate values of n.
    """

    intermediate_values = []
    steps = 0
    while n != 1:
        if n%2 == 0:
            n = n // 2
            intermediate_values.append(n)
        elif n%2 != 0:
            n = n*3 + 1 
            intermediate_values.append(n)
        steps += 1
    return  steps, intermediate_values


def main():
    while True:
        n = int(input("Input natural number: "))
        if n > 0:
            steps, intermediate_values = check_collatz_hypothesis(n)
            for value in intermediate_values:
                print(value, end=" ")
            print()
            print("Steps: {}".format(steps))
            print()
        else:
            print("Number must be > 0")


if __name__ == "__main__":
    main()
