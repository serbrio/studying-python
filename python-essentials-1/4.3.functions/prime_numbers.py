#!/usr/bin/env python3

def is_prime(num):
    for divisor in range(2, int(num ** 0.5 + 1)):
        if num % divisor == 0:
            return False
    return True


for i in range(1, 7399):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
