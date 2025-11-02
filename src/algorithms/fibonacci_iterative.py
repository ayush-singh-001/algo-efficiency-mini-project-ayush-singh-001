def fibonacci_iterative(n):
    """
    Calculate nth Fibonacci number using iteration.
    Args:
        n (int): Index of Fibonacci number to calculate.
    Returns:
        int: nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    print(fibonacci_iterative(10))  # Should print 55
