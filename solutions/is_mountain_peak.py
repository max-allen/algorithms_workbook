# a mountain peak is a list of consecutive
# integers that ascend to a peak, then decends

# [1, 2, 3, 4, 3, 2, 1] -> true
# [1, 2, 1, 4, 3, 2, 1] -> false
# [1, 2, 3, 4, 3, 4, 1] -> false


def is_mountain_peak(arr):
    peak = None
    prev = None

    while len(arr):
        curr = arr.pop(0)

        if prev is None:
            prev = curr

        if peak:
            if prev < curr:
                return False
        else:
            if curr < prev:
                peak = prev

        prev = curr

    return True
