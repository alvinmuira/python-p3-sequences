#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    a, b = 0, 1
    for _ in range(length):
        sequence.append(a)
        a, b = b, a + b
    print(sequence)

print_fibonacci(0)   # []
print_fibonacci(1)   # [0]
print_fibonacci(2)   # [0, 1]
print_fibonacci(10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

