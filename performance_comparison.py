# Name: Weevern Gong
# Project Title: MSCS532_Assignment3
# Description: This program compares the performance of Randomized Quick Sort and Deterministic Quick Sort using
# random, sorted, reverse-sorted, and repeated-value data. The program records the median execution time for each
# algorithm and saves the results to a CSV file.

# Performance comparison explanation: This program tests both quick sort algorithms with input sizes of 100, 500,
# 1000, and 2000 elements. Each input size is tested with random, sorted, reverse-sorted, and repeated-value data.
# The same input list is used for both algorithms during each comparison so that the pivot-selection method is the
# main difference between them. Each execution-time test is run five times, and the median time is recorded to reduce
# the effect of small timing differences between runs. The program also checks each sorted result against Python's
# expected ascending order before recording the measurement. The completed performance results are displayed in the
# terminal and saved to results.csv.


import csv
import random
import statistics
import sys
import time

from randomized_quicksort import deterministic_quick_sort
from randomized_quicksort import randomized_quick_sort


INPUT_SIZES = [100, 500, 1000, 2000]
NUMBER_OF_TRIALS = 5
RANDOM_SEED = 532
OUTPUT_FILE = "results.csv"

# Increase the recursion limit so the deterministic algorithm can process larger sorted and reverse-sorted inputs
sys.setrecursionlimit(10000)


def create_datasets(size, random_generator):

    # Create values in sorted order
    sorted_arr = list(range(size))

    # Create the same values in reverse-sorted order
    reverse_sorted_arr = list(reversed(sorted_arr))

    # Create the same values in random order
    random_arr = sorted_arr.copy()
    random_generator.shuffle(random_arr)

    # Create an input containing repeated values
    repeated_range = max(5, size // 20)
    repeated_arr = [random_generator.randint(0, repeated_range) for i in range(size)]

    return {
        "Random": random_arr,
        "Sorted": sorted_arr,
        "Reverse Sorted": reverse_sorted_arr,
        "Repeated Values": repeated_arr,
    }


def verify_sorted_result(original_arr, sorted_arr):

    # Compare the algorithm result with Python's expected ascending order
    expected_arr = sorted(original_arr)

    if sorted_arr != expected_arr:
        raise ValueError("The sorting algorithm produced an incorrect result.")


def measure_execution_time(sort_function, input_arr):

    execution_times = []

    # Run the same test several times and record each execution time
    for i in range(NUMBER_OF_TRIALS):
        test_arr = input_arr.copy()

        start_time = time.perf_counter()
        sort_function(test_arr)
        end_time = time.perf_counter()

        verify_sorted_result(input_arr, test_arr)

        execution_time_ms = (end_time - start_time) * 1000
        execution_times.append(execution_time_ms)

    # Use the median execution time so one unusually fast or slow run has less effect
    return statistics.median(execution_times)


def run_performance_comparison():

    algorithms = {
        "Randomized Quick Sort": randomized_quick_sort,
        "Deterministic Quick Sort": deterministic_quick_sort,
    }

    random_generator = random.Random(RANDOM_SEED)
    results = []

    # Test each required input size
    for size in INPUT_SIZES:
        datasets = create_datasets(size, random_generator)

        # Test random, sorted, reverse-sorted, and repeated-value data for each size
        for dataset_name, input_arr in datasets.items():

            # Run both algorithms on the same input arrangement
            for algorithm_name, sort_function in algorithms.items():

                median_time_ms = measure_execution_time(sort_function, input_arr)

                results.append(
                    {
                        "Algorithm": algorithm_name,
                        "Dataset": dataset_name,
                        "Input Size": size,
                        "Median Execution Time (ms)": round(median_time_ms, 6),
                    }
                )

    return results


def save_results(results):

    column_names = [
        "Algorithm",
        "Dataset",
        "Input Size",
        "Median Execution Time (ms)",
    ]

    # Write all performance results to results.csv
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as results_file:
        writer = csv.DictWriter(results_file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(results)


def print_results(results):

    # Print column headings for the performance results
    print(
        f"{'Algorithm':<26}"
        f"{'Dataset':<18}"
        f"{'Input Size':>12}"
        f"{'Median Time (ms)':>20}"
    )

    print("-" * 76)

    # Print one row for each performance result
    for result in results:
        print(
            f"{result['Algorithm']:<26}"
            f"{result['Dataset']:<18}"
            f"{result['Input Size']:>12}"
            f"{result['Median Execution Time (ms)']:>20.6f}"
        )


def main():

    results = run_performance_comparison()

    print_results(results)

    save_results(results)

    print("\nPerformance comparison results saved to results.csv")


if __name__ == "__main__":
    main()
