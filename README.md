# Analyzing and Visualizing Recursive Algorithm Efficiency

## Project Overview

This project analyzes and compares the performance of common recursive and iterative algorithms, focusing on time and space complexity trade-offs. Through empirical profiling and visualization, it demonstrates how algorithm design choices impact real-world performance.

## Algorithms Implemented

### 1. Fibonacci Sequence
- **Recursive Implementation**: Demonstrates exponential time complexity O(2^n)
- **Iterative Implementation**: Optimized linear time complexity O(n)

### 2. Sorting Algorithms
- **Bubble Sort**: O(n²) comparison-based sort
- **Selection Sort**: O(n²) with minimal swaps
- **Insertion Sort**: O(n²) efficient for small/partially sorted data
- **Merge Sort**: O(n log n) divide-and-conquer algorithm

### 3. Search Algorithm
- **Binary Search**: O(log n) search on sorted arrays

## Project Structure

```
algo-efficiency-mini-project-ayush-singh-001/
├── README.md                    # Project documentation
├── ANALYSIS.md                  # Detailed performance analysis
├── .gitignore                   # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── profile_all_algorithms.py   # Main profiling script
│   └── algorithms/
│       ├── fibonacci_recursive.py
│       ├── fibonacci_iterative.py
│       ├── bubble_sort.py
│       ├── selection_sort.py
│       ├── insertion_sort.py
│       ├── merge_sort.py
│       └── binary_search.py
└── plots/*.png                        # Performance visualization plots
```

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

1. Clone the repository:
```
git clone https://github.com/your-username/algo-efficiency-mini-project-ayush-singh-001.git
cd algo-efficiency-mini-project-ayush-singh-001
```

2. Create and activate virtual environment:
```
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```
pip install matplotlib memory-profiler
```

## Running the Project

### Test Individual Algorithms
```
python src/algorithms/fibonacci_recursive.py
python src/algorithms/bubble_sort.py
# ... etc for other algorithms
```

### Run Complete Profiling Analysis
```
python src/profile_all_algorithms.py
```

This will:
- Profile execution time and memory usage for all algorithms
- Generate comparative visualization plots
- Display results in separate plot windows

## Key Findings

### Performance Insights
- **Recursive Fibonacci** becomes impractical beyond n=35 due to exponential time complexity
- **Iterative Fibonacci** handles large inputs efficiently with linear complexity
- **Merge Sort** significantly outperforms O(n²) algorithms on datasets larger than ~500 elements
- **Binary Search** demonstrates logarithmic efficiency even on very large sorted arrays

### Trade-offs
- **Time vs Space**: Merge sort trades memory (O(n)) for speed (O(n log n))
- **Simplicity vs Efficiency**: Simple algorithms like bubble sort are easy to understand but inefficient
- **Recursion Limits**: Python's recursion depth limit (~1000) affects recursive implementations

See [ANALYSIS.md](ANALYSIS.md) for detailed performance analysis and recommendations.

## Visualizations

The project generates three sets of plots:
1. **Fibonacci Comparison**: Shows exponential vs linear growth
2. **Sorting Algorithms**: Compares O(n²) vs O(n log n) performance
3. **Binary Search**: Demonstrates logarithmic search efficiency

## Learning Objectives Achieved

✅ Applied algorithmic characteristics (finiteness, effectiveness, input/output)  
✅ Visualized time and space trade-offs through empirical profiling  
✅ Analyzed practical impact of algorithm design decisions  
✅ Documented findings with proper technical communication  

## References

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Python `time` module documentation: https://docs.python.org/3/library/time.html
- Python `memory_profiler` package: https://pypi.org/project/memory-profiler/

## Author

Ayush Singh - Algorithm Efficiency Analysis Project

## License

This project is for educational purposes as part of an algorithm analysis assignment.
