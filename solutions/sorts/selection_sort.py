from .utils import swap


def selection_sort(arr):
    for curr_idx in range(len(arr) - 1):
        min_index = curr_idx

        for nxt_idx in range(curr_idx + 1, len(arr)):
            if arr[nxt_idx] < arr[min_index]:
                min_index = nxt_idx

        swap(arr, curr_idx, min_index)

    return arr
