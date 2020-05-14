#!/usr/bin/env python3

"""Calculate Mean for the given list"""


def mean(numbers):
    return int(sum(numbers) / len(numbers))


if __name__ == "__main__":
    steps = [4000, 3200, 3860, 4090, 3710, 2069, 987]
    mean = mean(steps)

    print("Your average step/day is:", mean)
