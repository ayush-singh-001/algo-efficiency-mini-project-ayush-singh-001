# Algorithm Performance Analysis

## 1. Fibonacci Algorithms

### Fibonacci Recursive
- **Time Complexity**: O(2^n) - Exponential growth due to redundant calculations
- **Space Complexity**: O(n) - Call stack depth equals n
- **Observations**: Execution time grows exponentially. Even for n=30, runtime becomes significant (several seconds).
- **Recursion Depth Issue**: Python has a default recursion limit of ~1000. For large n values, this algorithm will hit RecursionError.
- **Trade-offs**: Simple to implement and understand, but highly inefficient for larger inputs.

### Fibonacci Iterative
- **Time Complexity**: O(n) - Linear, single pass through loop
- **Space Complexity**: O(1) - Only stores two variables
- **Observations**: Execution time grows linearly and remains fast even for large n values.
- **Trade-offs**: Slightly more complex logic than recursive version, but dramatically more efficient for practical use.

### Comparison
The iterative approach is vastly superior for Fibonacci calculation. The recursive version demonstrates the pitfalls of naive recursion without memoization.

## 2. Sorting Algorithms

### Bubble Sort
- **Time Complexity**: O(n²) - Nested loops with comparisons
- **Space Complexity**: O(1) - In-place sorting
- **Observations**: Performance degrades quickly with input size. Slowest among implemented algorithms.
- **Best Use Case**: Educational purposes, very small datasets, or nearly sorted data.

### Selection Sort
- **Time Complexity**: O(n²) - Always performs n² comparisons
- **Space Complexity**: O(1) - In-place sorting
- **Observations**: Slightly better than bubble sort in practice due to fewer swaps.
- **Best Use Case**: When memory writes are expensive (fewer swaps than bubble sort).

### Insertion Sort
- **Time Complexity**: O(n²) worst case, O(n) best case for nearly sorted data
- **Space Complexity**: O(1) - In-place sorting
- **Observations**: More efficient than bubble/selection sort on partially sorted data.
- **Best Use Case**: Small datasets or nearly sorted arrays.

### Merge Sort
- **Time Complexity**: O(n log n) - Divide and conquer approach
- **Space Complexity**: O(n) - Requires additional arrays for merging
- **Observations**: Consistently fast regardless of input distribution. Significantly outperforms O(n²) algorithms.
- **Best Use Case**: Large datasets where consistent performance is needed.

### Comparison
Merge sort clearly dominates for larger datasets due to its O(n log n) complexity. The O(n²) algorithms (bubble, selection, insertion) become impractical beyond a few thousand elements.

## 3. Binary Search

- **Time Complexity**: O(log n) - Halves search space each iteration
- **Space Complexity**: O(1) - Iterative implementation with constant space
- **Observations**: Extremely fast even for very large sorted arrays.
- **Requirement**: Array must be pre-sorted.
- **Best Use Case**: Searching in large sorted datasets.

## 4. Key Insights

### Recursion Depth Challenges
- Recursive Fibonacci demonstrates the danger of deep recursion in Python
- Default recursion limit can be increased using `sys.setrecursionlimit()`, but this is not recommended
- Iterative solutions or memoization are preferred

### Time vs Space Trade-offs
- Merge sort uses O(n) extra space but achieves O(n log n) time
- In-place sorts (bubble, selection, insertion) use O(1) space but have O(n²) time
- Choice depends on whether time or space is the limiting resource

### Algorithm Selection Guidelines
- **Small datasets (n < 100)**: Simple algorithms like insertion sort are acceptable
- **Large datasets**: Use O(n log n) algorithms like merge sort
- **Memory constraints**: Prefer in-place algorithms
- **Fibonacci calculation**: Always use iterative or memoized approach

## 5. Practical Impact

Understanding these performance characteristics is critical for real-world software engineering:
- Web applications processing user data need efficient sorting
- Financial systems calculating sequences need optimal algorithms
- Search functionality requires understanding of logarithmic performance
- Recursive algorithms must be carefully evaluated for depth limits
