#!/usr/bin/python3
""" FizzBuzz """

import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - If a number is divisible by three, it prints "Fizz" instead of
    the number.
    - If a number is divisible by five, it prints "Buzz" instead of
    the number.
    - If a number is divisible by both three and five, it prints "FzzBuzz".
    """

    if n < 1:
        return

    output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
             output.append(str(i))

    print(" ".join(output))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Invalid number")
        sys.exit(1)

    fizzbuzz(number)
