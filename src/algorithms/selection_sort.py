def selection_sort(arr):
    """
    Sorts an array using selection sort algorithm.
    Args:
        arr (list): List of elements to be sorted.
    Returns:
        list: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print(selection_sort(sample))  # Should print sorted list
