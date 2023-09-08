## Arrays

The fundamental [[contiguously-allocated]] data structure. These data records
are of fixed size. Consequently, each element can be located by its numeric
index. Arrays come in two flavors: **static** (fixed size), and **dynamic**.
Arrays offered first class by interpreted languages (e.g. JavaScript, Python)
are implemented dynamically.

**Use Cases**:
- [Stacks](#stacks-queues)
- [Queues](#stacks-queues)
- Graphs (Adjacency Lists)

**Advantages**:
- Constant time access to elements provided the index is known (efficient random
  access).
- Space efficient as it doesn't use pointers.
- Contiguous allocation allows for better memory locality and cache performance.

**Drawbacks**:
- Less efficient, complex insertion in comparison to Linked Lists.
- Overflow is possible when writing to or attempting to access static arrays.
- With large records, moving pointers instead of the items themselves is faster
  and easier.

**Standard Operations:**

| **Operation** | **Time Complexity** |
| -------- | -------- |
| **Access** | **O(1)** |
| **Update** | **O(1)** |
| **Insert / Remove** | **O(N)** |
| **Insert (Size Reached)** | **Amortized O(1) dynamic; O(N) static** |
| **Remove (End)** | **O(1)** |
| **Search** | **O(N)** |

