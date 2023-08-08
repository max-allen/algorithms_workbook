def swap(arr, prev_idx, curr_idx):
    prev_value, curr_value = arr[prev_idx], arr[curr_idx]
    arr[prev_idx], arr[curr_idx] = curr_value, prev_value
    return arr


def insertion_sort(arr):
    sorted_idx = 1

    while sorted_idx < len(arr):
        curr_idx = sorted_idx
        while curr_idx > 0 and arr[curr_idx - 1] > arr[curr_idx]:
            swap(arr, curr_idx - 1, curr_idx)
            curr_idx -= 1
        sorted_idx += 1

    return arr
