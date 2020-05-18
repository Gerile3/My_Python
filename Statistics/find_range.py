#!/usr/bin/env python3

'''Find the range'''


def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    # Find the range
    r = highest - lowest

    return lowest, highest, r


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('Lowest: {} Highest: {} Range: {}'.format(lowest, highest, r))
