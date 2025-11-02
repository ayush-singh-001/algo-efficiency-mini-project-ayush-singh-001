import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

from algorithms.fibonacci_recursive import fibonacci_recursive
from algorithms.fibonacci_iterative import fibonacci_iterative
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.binary_search import binary_search

def profile_algorithm(func, inputs):
    """Profile execution time and memory for a function with various inputs."""
    times, memories = [], []

    for inp in inputs:
        # Time profiling
        start_time = time.perf_counter()
        if isinstance(inp, tuple):
            func(*inp)
        else:
            func(inp)
        end_time = time.perf_counter()
        times.append(end_time - start_time)

        # Memory profiling
        mem_usage = memory_usage((func, inp if isinstance(inp, tuple) else (inp,)), max_iterations=1)
        memories.append(max(mem_usage) - min(mem_usage))
    
    return times, memories

if __name__ == '__main__':
    # Smaller input sizes for faster profiling
    fib_sizes = list(range(5, 31, 5))  # 5, 10, 15, 20, 25, 30
    sort_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    
    # Prepare inputs for each algorithm
    fib_inputs = [(n,) for n in fib_sizes]
    sort_inputs = [[i for i in range(size, 0, -1)] for size in sort_sizes]  # Worst case: reverse sorted
    search_inputs = [([i for i in range(1000)], 999)] * len(sort_sizes)
    
    # Profile each algorithm with progress indication
    results = {}
    
    print("Profiling Fibonacci Recursive...")
    results['Fibonacci Recursive'] = profile_algorithm(fibonacci_recursive, fib_inputs)
    
    print("Profiling Fibonacci Iterative...")
    results['Fibonacci Iterative'] = profile_algorithm(fibonacci_iterative, fib_inputs)
    
    print("Profiling Bubble Sort...")
    results['Bubble Sort'] = profile_algorithm(bubble_sort, sort_inputs)
    
    print("Profiling Selection Sort...")
    results['Selection Sort'] = profile_algorithm(selection_sort, sort_inputs)
    
    print("Profiling Insertion Sort...")
    results['Insertion Sort'] = profile_algorithm(insertion_sort, sort_inputs)
    
    print("Profiling Merge Sort...")
    results['Merge Sort'] = profile_algorithm(merge_sort, sort_inputs)
    
    print("Profiling Binary Search...")
    results['Binary Search'] = profile_algorithm(binary_search, search_inputs)
    
    print("Profiling complete! Generating plots...")
    
    # Create separate plots for Fibonacci and Sorting algorithms
    # Plot 1: Fibonacci algorithms
    fig1, axes1 = plt.subplots(1, 2, figsize=(14, 5))
    
    for idx, name in enumerate(['Fibonacci Recursive', 'Fibonacci Iterative']):
        times, memories = results[name]
        ax1 = axes1[idx]
        
        color = 'tab:blue'
        ax1.set_xlabel('Input Size (n)')
        ax1.set_ylabel('Time (seconds)', color=color)
        ax1.plot(fib_sizes, times, color=color, marker='o', label='Time')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_title(f'{name}')
        ax1.grid(True, alpha=0.3)
        
        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Memory (MB)', color=color)
        ax2.plot(fib_sizes, memories, color=color, marker='x', label='Memory')
        ax2.tick_params(axis='y', labelcolor=color)
    
    plt.tight_layout()
    
    # Plot 2: Sorting algorithms
    fig2, axes2 = plt.subplots(2, 2, figsize=(14, 10))
    axes2 = axes2.flatten()
    
    sorting_algos = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort']
    
    for idx, name in enumerate(sorting_algos):
        times, memories = results[name]
        ax1 = axes2[idx]
        
        color = 'tab:blue'
        ax1.set_xlabel('Input Size (array length)')
        ax1.set_ylabel('Time (seconds)', color=color)
        ax1.plot(sort_sizes, times, color=color, marker='o', label='Time')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_title(f'{name}')
        ax1.grid(True, alpha=0.3)
        
        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Memory (MB)', color=color)
        ax2.plot(sort_sizes, memories, color=color, marker='x', label='Memory')
        ax2.tick_params(axis='y', labelcolor=color)
    
    plt.tight_layout()
    
    # Plot 3: Binary Search
    fig3, ax = plt.subplots(1, 1, figsize=(8, 5))
    times, memories = results['Binary Search']
    
    color = 'tab:blue'
    ax.set_xlabel('Number of Searches')
    ax.set_ylabel('Time (seconds)', color=color)
    ax.plot(range(len(sort_sizes)), times, color=color, marker='o', label='Time')
    ax.tick_params(axis='y', labelcolor=color)
    ax.set_title('Binary Search')
    ax.grid(True, alpha=0.3)
    
    ax2 = ax.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Memory (MB)', color=color)
    ax2.plot(range(len(sort_sizes)), memories, color=color, marker='x', label='Memory')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.tight_layout()

    # Save plots
    fig1.savefig('plots/fibonacci_comparison.png')
    fig2.savefig('plots/sorting_comparison.png')
    fig3.savefig('plots/binary_search_profile.png')

    plt.show()
    
    print("All plots displayed!")
