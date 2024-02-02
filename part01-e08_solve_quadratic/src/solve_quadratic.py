#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    x1 = (((-b) + math.sqrt( (b** 2) - (4 * a * c) )) / (2 * a))
    x2 = (((-b) - math.sqrt( (b** 2) - (4 * a * c) )) / (2 * a))
    return (x1,x2)


def main():
    pass
    a = float(input("give the a value: "))
    b = float(input("give the b value: "))
    c = float(input("give the c value: "))
    result = solve_quadratic(a, b, c)
    print(result)

if __name__ == "__main__":
    main()
