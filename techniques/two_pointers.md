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

### Exercises:

- [three_number_sum](/arrays/three_number_sum.py)
