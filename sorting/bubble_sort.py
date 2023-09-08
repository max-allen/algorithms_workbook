# O(N^2) Time Complexity | O(1) Space Complexity
from .utils import swap


def bubble_sort(arr):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for idx in range(len(arr) - 1):
            nxt_idx = idx + 1

            if arr[nxt_idx] < arr[idx]:
                is_sorted = False
                swap(arr, idx, nxt_idx)

    return arr
