#!/usr/bin/env python3

import matplotlib.pyplot as plt


def correlation(list1, list2):
    n = len(list1)
    sum_xy = sum([x * y for x, y in zip(list1, list2)])
    sum_x = sum(list1)
    sum_y = sum(list2)
    sum_x2 = sum([x**2 for x in list1])
    sum_y2 = sum([y**2 for y in list2])

    corr = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x2 - (sum_x)**2) * (n * sum_y2 - (sum_y)**2))**0.5

    return corr


if __name__ == "__main__":
    list1 = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
    list2 = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

    correlation = correlation(list1, list2)

    print("Correlation coefficient of the two lists: {:.2f}".format(correlation))

    # if plot closer to be diagonal that means correlation is high,
    # strong relationship between these data set
    plt.scatter(list1, list2)
    plt.grid()
    plt.show()
