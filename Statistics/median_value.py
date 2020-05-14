#!/usr/bin/env python3

'''Calculating the median'''


def median(numbers):
    numbers.sort()

    if len(numbers) % 2 == 0:
        n1 = numbers[(len(numbers) // 2) - 1]
        n2 = numbers[len(numbers) // 2]
        med = (n1 + n2) // 2
    else:
        med = numbers[len(numbers) // 2]

    return med


if __name__ == "__main__":
    steps = [4000, 3200, 3860, 4090, 3710, 2069, 987, 1000]
    median = median(steps)

    print("Median of your steps:", median)
