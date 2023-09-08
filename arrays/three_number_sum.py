# Given a non empty array of distinct integers and a target integer, return
# a two dim array of all triplets that sum to the target. Triplets should be
# ordered ascending.

# [12, 3, 1, 2, -6, 5, -8, 6], 0 -> [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]


def three_number_sum(arr, target):
    result = []
    arr.sort()

    for idx in range(0, len(arr) - 2):
        curr = arr[idx]
        left_idx = idx + 1
        right_idx = len(arr) - 1

        while left_idx < right_idx:
            left = arr[left_idx]
            right = arr[right_idx]
            total = left + right + curr

            if total == target:
                result.append([curr, left, right])
                left_idx += 1
                right_idx -= 1

            elif total < target:
                left_idx += 1

            elif total > target:
                right_idx -= 1

    return result
