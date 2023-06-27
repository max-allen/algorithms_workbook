# Given a non empty array of distinct integers and a target integer, return any
# pair of integers that sum to the target.

# [5, 3, 2, -3, 0], 7 -> [5, 2] or [2, 5]


def two_number_sum(nums, target):
    mutable = nums.copy()
    el = mutable.pop(0)

    comp = target - el

    if comp in mutable:
        return [el, comp]

    elif len(mutable) > 1:
        return two_number_sum(mutable, target)

    return []
