#!/usr/bin/env python3
"""Binary search implementation in python"""


def binary_search(array, element, silent=False):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        if not silent:
            print("Subarray in step {}: {}".format(step, str(array[start:end + 1])))
        step = step + 1
        mid = (start + end) // 2

        try:
            if element == array[mid]:
                return mid, step

            if element < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        except IndexError:
            return False

    return False


if __name__ == "__main__":
    array = list(range(1000))
    element = int(input("Enter the number to search: "))
    result = binary_search(array, element)  # call with silent=True to hide subarrays

    if result:
        print(f"Found! {result[0]} is in array. It took {result[1]} steps to find it.")
    else:
        print("Not found")
