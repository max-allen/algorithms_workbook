from .utils import swap


def insertion_sort(arr):
    sorted_idx = 1

    while sorted_idx < len(arr):
        curr_idx = sorted_idx
        while curr_idx > 0 and arr[curr_idx - 1] > arr[curr_idx]:
            swap(arr, curr_idx - 1, curr_idx)
            curr_idx -= 1
        sorted_idx += 1

    return arr
