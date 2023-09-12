## Linked Lists

The fundamental linked data structure. Unlike their [[contiguously-allocated]],
counterpart, [arrays](#arrays), memory is allocated dynamically,
and their elements consequently have no index or order beyond head and tail
nodes. Elements are connected by pointers, which represent the address of a
location in memory. Linked Lists most commonly come in two flavors: **singly**
and **doubly** linked. Linked lists are a specialized data structure that may or
may not have first class support in a language.

**Use Cases**:
- Stacks
- Queues
- Graphs (Adjacency Lists)

 **Advantages**:
- Unlike static arrays, overflow can never occur.
- Simple insertion and deletion.
- Work well with large records as moving pointers is easier and faster than
  moving the record itself.

**Drawbacks**:
- Inefficient random access given lack of indices.
- Pointers require space consumption.

**Standard Operations:**

| **Operation** | **Time Complexity** |
| -------- | -------- |
| **Access (head/tail)** | **O(1)** |
| **Access / Search (non-head/tail)** | **O(N)** |
| **Insert / Remove (head/tail)** | **O(1)** |
| **Insert / Remove before/after non-head/tail node** | **O(N)** |

- **Note:** Singly linked lists have no tail pointer, so access to final element
  is **O(N)**.