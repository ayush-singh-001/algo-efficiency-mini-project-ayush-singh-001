def insertion_sort(arr):
    """
    Sorts an array using insertion sort algorithm.
    Args:
        arr (list): List of elements to be sorted.
    Returns:
        list: Sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6]
    print(insertion_sort(sample))  # Should print sorted list
