#!/usr/bin/env python3
from find_range import find_range
from find_variance import variance, std_deviation
from mean_value import mean
from mode_value import mode


def calculator(numbers):
    min_max = find_range(numbers)
    var = variance(numbers)
    std = std_deviation(numbers)
    mean_val = mean(numbers)
    mode_val = mode(numbers)

    results = [min_max, var, std, mean_val, mode_val]

    return results


if __name__ == "__main__":
    filename = input("Enter the filename(without extension, currently only supports .txt files): ")
    try:
        with open("{}.txt".format(filename), "r") as f:
            x = f.read().split(",")
    except IOError:
        print("File not found or wrong file")

    numbers = [int(i) for i in x]
    result = calculator(numbers)

    print("Lowest value: {}, Highest Value: {}, Range: {}, Variance: {:.2f}, Standart Deviation: {:.2f}, Mean: {}, Mode(s): {}".format(result[0][0],
          result[0][1], result[0][2], result[1], result[2], result[3], result[4]))

    # Todo:
    # Better layout
    # get results inside dict maybe for better accessibility
    # Make class instead importing(?)
