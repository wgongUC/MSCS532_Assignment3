# MSCS532_Assignment3 by Weevern Gong

## Description
This project implements Randomized Quick Sort, Deterministic Quick Sort, and a Hash Table with Chaining using Python. Randomized Quick Sort selects pivots randomly, while Deterministic Quick Sort always uses the first value in the current portion as the pivot. A performance comparison program tests both sorting algorithms using random, sorted, reverse-sorted, and repeated-value data. The hash table supports insert, search, and delete operations, uses chaining to resolve collisions, and dynamically resizes when the load factor becomes too high.

## Requirements
- Python 3.8 or higher
- Visual Studio Code or alternate IDE
- Python extension for Visual Studio Code
- Git (to clone repository)
- GitHub account (to fork repository to own GitHub account, etc.)
- Code Runner extension (optional requirement)

## Instructions
1. Go to the GitHub repository at https://github.com/wgongUC/MSCS532_Assignment3

2. Select either option 1 or option 2:

Option 1: Download ZIP File
- Click on the green button "Code" and select "Download ZIP".
- Extract the downloaded ZIP file, then open Visual Studio Code and select File > Open Folder.
- Select the folder containing randomized_quicksort.py, hash_table_chaining.py, and performance_comparison.py.

Option 2: Clone with Git
- Click on the green button "Code", and select the HTTPS tab. Click "Copy URL to clipboard" on the right to copy the URL https://github.com/wgongUC/MSCS532_Assignment3.git.
- In Windows, open a terminal window and run this command:
    ```bash
    git clone https://github.com/wgongUC/MSCS532_Assignment3.git
    ```
- A new project folder will be created in the current terminal location.
- In Visual Studio Code, select File > Open Folder and select the project folder that was created.

3. To run the Randomized Quick Sort and Deterministic Quick Sort program in Visual Studio Code, select Terminal > New Terminal and run the following command:
    ```bash
    python randomized_quicksort.py
    ```

The terminal will display the input list and the list sorted in monotonically increasing order using both versions of Quick Sort.

4. To run the Hash Table with Chaining program, run the following command:
    ```bash
    python hash_table_chaining.py
    ```

The terminal will display the table after inserting sample key-value pairs, show collision resolution through chaining, perform successful and unsuccessful searches, delete a key from a chain, and display the updated hash table.

5. To run the performance comparison, run the following command:
    ```bash
    python performance_comparison.py
    ```

The performance comparison tests random, sorted, reverse-sorted, and repeated-value inputs containing 100, 500, 1000, and 2000 elements. Each execution-time test is run five times and the median is recorded. The same input arrangement is used for both Quick Sort algorithms during each comparison. The complete results are displayed in the terminal and saved to results.csv.

6. To test the sorting algorithms with custom inputs, edit the numbers in the numbers_arr array in randomized_quicksort.py, then save the program file and run it.

7. To test the hash table with custom values, edit the insert, search, and delete operations in the main function of hash_table_chaining.py, then save the program file and run it.

## Example Input
[5, 2, 20, 9, 1, 5, 6, 3, 71, 8, 4, 56, 12]

## Example Output
[1, 2, 3, 4, 5, 5, 6, 8, 9, 12, 20, 56, 71]

## Summary of Findings
The performance comparison showed that Randomized Quick Sort was much less affected by the original order of the input values than Deterministic Quick Sort. At an input size of 2000, Randomized Quick Sort required 1.0356 ms for sorted data and 1.0016 ms for reverse-sorted data, while Deterministic Quick Sort required 29.0300 ms and 51.9253 ms, respectively. On random and repeated-value inputs, the two algorithms were much closer, and Deterministic Quick Sort was slightly faster in several tests. The additional random pivot selection used by Randomized Quick Sort can contribute some execution overhead.

The Hash Table with Chaining successfully handled collisions by storing multiple key-value pairs in the same table slot. The sample execution placed several keys into one chain, and search and delete operations correctly accessed an individual value without affecting the other values in the chain. Dynamic resizing also increased the table capacity when the load factor exceeded 0.75.

## Time Complexity
Randomized Quick Sort has expected time complexity of Θ(n log n). Its worst-case time complexity is Θ(n²).

Deterministic Quick Sort has best-case time complexity of Θ(n log n). Its worst-case time complexity is Θ(n²), and repeatedly unbalanced partitions can occur with sorted or reverse-sorted input when the first value is always selected as the pivot.

For hashing with chaining, search, insert, and delete operations have expected time complexity of Θ(1 + α), where α is the load factor. When the load factor remains bounded, these operations have expected Θ(1) time. Dynamic resizing occasionally requires rehashing the stored elements, but it prevents the average chain length from continuing to increase as more values are inserted.

## References
Carter, J. L., & Wegman, M. N. (1979). Universal classes of hash functions. *Journal of Computer and System Sciences, 18*(2), 143–154. https://doi.org/10.1016/0022-0000(79)90044-8

Hoare, C. A. R. (1962). Quicksort. *The Computer Journal, 5*(1), 10–16. https://doi.org/10.1093/comjnl/5.1.10

Sedgewick, R. (1977). Quicksort with equal keys. *SIAM Journal on Computing, 6*(2), 240–267. https://doi.org/10.1137/0206018
