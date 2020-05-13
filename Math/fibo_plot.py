#!/usr/bin/env python3
"""
A program that will plot on a graph the ratio between consecutive Fibonacci numbers (for the first 50 numbers),
which will demonstrate that the values approach the golden ratio.
"""
import matplotlib.pyplot as plt


def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series


def plot_fibo(numbers):
    length = range(len(numbers) - 1)
    ratios = []

    for i in length:
        if i + 1 < len(numbers):
            ratios.append(numbers[i + 1] / numbers[i])

    plt.plot(length, ratios)
    plt.title("Ratio between consecutive fibonacci numbers")
    plt.xlabel("No.")
    plt.ylabel("Ratio")
    plt.show()


if __name__ == "__main__":
    numbers = fibonacci(50)
    plot_fibo(numbers)
