def quick_sort(arr):
    """
    Sorts an array using quick sort algorithm.
    Args:
        arr (list): List of elements to be sorted.
    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print(quick_sort(sample))  # Should print sorted list
