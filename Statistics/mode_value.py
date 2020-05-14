#!/usr/bin/env python3
'''Calculating the mode'''

from collections import Counter


def mode(numbers):
    nums = []
    c = Counter(numbers)
    freq = c.most_common()
    max_occurence = c.most_common(1)[0][1]

    for num in freq:
        if num[1] == max_occurence:
            nums.append(num)

    return nums


def mode_table(numbers, show=True):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()

    if show:
        print('Number\tFrequency')
        for number in numbers_freq:
            print('{0}\t{1}'.format(number[0], number[1]))

    return numbers_freq


if __name__ == "__main__":
    values = [5, 5, 5, 4, 4, 4, 9, 1, 3, 9]
    mode = mode(values)

    for i in range(len(mode)):
        print("Most common value: {}, and the number of occurences: {}".format(mode[i][0], mode[i][1]))

    mode_table(values)
