#!/usr/bin/env python3
import pandas as pd
import numpy as np


def multiples(number, limit=11):
    """Prints out multiplications for the given number"""
    for i in range(1, limit):
        print('{0} x {1} = {2}'.format(number, i, number * i))


def multiples_table(limit=11):
    """Prints out multiplication table till the given number"""
    listo = list(range(1, limit + 1))
    multy = np.array([i * y for i in listo for y in listo]).reshape(limit, limit)
    df = pd.DataFrame(multy)
    df.index = np.arange(1, len(df) + 1)
    df.columns = np.arange(1, len(df) + 1)
    print(df)


if __name__ == '__main__':
    print("1. List\n2. Table")
    try:
        choice = int(input())
        if choice == 1:
            number = int(input('Enter a number: '))
            multiples(number)
        if choice == 2:
            number = int(input('Enter a number: '))
            multiples_table(number)
    except ValueError:
        print("Enter Number!")
