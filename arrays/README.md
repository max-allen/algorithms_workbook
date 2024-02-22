## Arrays

The fundamental contiguously-allocated data structure. These data records
are of fixed size. Consequently, each element can be located by its numeric
index. Arrays come in two flavors: **static** (fixed size), and **dynamic**.
Arrays offered first class by interpreted languages (e.g. JavaScript, Python)
are implemented dynamically.

## Related Structures

- Arrays are used as a primitive to compose: [stacks](/stacks/README.md),
  [queues](/queues/README.md), and [graphs](/graphs/README.md).

- [Strings](/strings/README.md) are sequences of characters implemented using
  an array or similar structure. Many array techniques can used with strings.

## Relevant Concepts

**Subarray**

A range of contiguous values within an array.

`[3, 6, 1]` is valid subarray of `[2, 3, 6, 1, 5, 4]`.

**Subsequence**

A sequence that can be derived from the given sequence by deleting some or no
elements without changing the order of the remaining elements.

`[3, 1, 5]` is valid subsequence `[2, 3, 6, 1, 5, 4]`.

## Time Complexities

| Operation | Big-O |
| --------- | ----- |
| Access    | O(1)  |
| Search    | O(N)  |

## Considerations

- **Duplicate values**: Consider a sorting algorithm that needs to find
  subsets of elements meeting some criteria. Would duplicate values affect its
  correctness?
