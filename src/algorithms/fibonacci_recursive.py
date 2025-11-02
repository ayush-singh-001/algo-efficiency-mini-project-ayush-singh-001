def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number using recursion.
    Args:
        n (int): Index of Fibonacci number to calculate.
    Returns:
        int: nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if __name__ == "__main__":
    print(fibonacci_recursive(10))  # Should print 55
