# Name: Weevern Gong
# Project Title: MSCS532_Assignment3
# Description: This program implements randomized quick sort and deterministic quick sort to sort a list of integers
# in monotonically increasing order. Randomized quick sort selects a pivot randomly, while deterministic quick sort
# always uses the first value in the current portion as the pivot.

# Randomized quick sort explanation: Randomized quick sort works by randomly selecting a pivot from the current portion
# of the list and dividing the values around that pivot. Values that are less than or equal to the pivot are moved to
# its left, while larger values remain on its right. The algorithm recursively repeats this process on both sides of
# the pivot until the entire list is sorted.
# Deterministic quick sort uses the same partitioning process, but always selects the first value in the current portion
# as the pivot. This makes its performance more dependent on the order of the input values.
# Both algorithms sort the list in place. Randomized quick sort has expected time complexity Θ(n log n) and worst-case
# time complexity Θ(n^2). Deterministic quick sort also has worst-case time complexity Θ(n^2).


import random


def partition(arr, low, high):

    # Use the last value in the current portion as the pivot during partitioning
    pivot = arr[high]
    i = low - 1

    # Move values less than or equal to the pivot toward the left side
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Move the pivot after the values that are less than or equal to it
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def deterministic_quick_sort(arr):

    # Sort the entire list from the first index to the last index
    deterministic_quick_sort_recursive(arr, 0, len(arr) - 1)

    return arr


def deterministic_quick_sort_recursive(arr, low, high):

    # Continue partitioning while the current portion contains more than one element
    if low < high:

        # Move the first value to the last position so it can be used as the pivot
        arr[low], arr[high] = arr[high], arr[low]

        # Partition the current portion and place the pivot into its final sorted position
        pivot_index = partition(arr, low, high)

        # Recursively sort the values to the left of the pivot
        deterministic_quick_sort_recursive(arr, low, pivot_index - 1)

        # Recursively sort the values to the right of the pivot
        deterministic_quick_sort_recursive(arr, pivot_index + 1, high)


def randomized_quick_sort(arr):

    # Sort the entire list from the first index to the last index
    randomized_quick_sort_recursive(arr, 0, len(arr) - 1)

    return arr


def randomized_quick_sort_recursive(arr, low, high):

    # Continue partitioning while the current portion contains more than one element
    if low < high:

        # Randomly select a pivot from the current portion of the list
        random_pivot_index = random.randint(low, high)

        # Move the randomly selected pivot to the last position before partitioning
        arr[random_pivot_index], arr[high] = arr[high], arr[random_pivot_index]

        # Partition the current portion and place the pivot into its final sorted position
        pivot_index = partition(arr, low, high)

        # Recursively sort the values to the left of the pivot
        randomized_quick_sort_recursive(arr, low, pivot_index - 1)

        # Recursively sort the values to the right of the pivot
        randomized_quick_sort_recursive(arr, pivot_index + 1, high)


def main():

    numbers_arr = [5, 2, 20, 9, 1, 5, 6, 3, 71, 8, 4, 56, 12]

    print("Input array:", numbers_arr)

    randomized_arr = randomized_quick_sort(numbers_arr.copy())
    deterministic_arr = deterministic_quick_sort(numbers_arr.copy())

    print("Array sorted in monotonically increasing order using Randomized Quick Sort:", randomized_arr)
    print("Array sorted in monotonically increasing order using Deterministic Quick Sort:", deterministic_arr)


if __name__ == "__main__":
    main()
