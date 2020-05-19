#!/usr/bin/env python3
from mean_value import mean


def variance(numbers):
    result = []
    mean_val = mean(numbers)

    for number in numbers:
        result.append((number - mean_val)**2)

    var = sum(result) / len(numbers)

    return var


def std_deviation(var):
    return var**0.5


if __name__ == "__main__":
    notes = [90, 56, 45, 60, 72, 75, 38, 40, 52]

    variance = variance(notes)
    std = std_deviation(variance)

    print("Variance of notes: {:.2f}".format(variance))
    print("Standart deviation of notes {:.2f}".format(std))
