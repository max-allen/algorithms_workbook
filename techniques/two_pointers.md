# Two Pointers

## Use Cases

- Search algorithms that need to retrieve a subset of elements meeting
certain criteria.

- **Structures**: Arrays and array based structures.

## Example Usage

```py
def two_pointer_search(arr, target):
    arr.sort()
    left_idx, right_idx = 0, len(arr) - 1

    while left_idx != right_idx:
        left, right = arr[left_idx], arr[right_idx]

        nums = [left, right]
        total = sum(nums)

        if total == target:
            return nums

        elif total < target:
            left_idx += 1

        elif total > target:
            right_idx -= 1
```

## Considerations

Because the algorithm relies on sorted sequences, it may not be suited for
searches where the indicies of matching elements are desired. Consider the
application to [two_sum](/arrays/two_sum.py):

```py
def two_sum(arr, target):
    nums = sorted(arr)

    left_idx, right_idx = 0, len(nums) - 1

    while left_idx < right_idx:
        left, right = nums[left_idx], nums[right_idx]
        total = left + right

        if total == target:
            return [arr.index(left), arr.index(right)]

        elif total < target:
            left_idx += 1

        elif total > target:
            right_idx -= 1

    return []
```

The indicies of the input array must be preserved for retrieval later. The
index lookup increases the time complexity to O(N^3).


### Exercises:

- [three_number_sum](/arrays/three_number_sum.py)
- [two_number_sum](/arrays/two_sum.py)
