def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.
    Returns:
        int: Index of target if found, else -1.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7]
    print(binary_search(sample, 4))  # Should print 3
