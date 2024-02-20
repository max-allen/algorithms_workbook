# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def two_sum(nums, target):
    visited = {}

    for idx, num in enumerate(nums):
        comp = target - num

        if comp in visited:
            return [visited[comp], idx]

        visited[nums] = idx
