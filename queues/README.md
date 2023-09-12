<!-- # TODO: Revise to Queues Only -->
## Stacks, Queues

Stacks and Queues are collections of sequenced data that permit storage and
retrieval independent of content. These structures are distinguished by their
**retrieval order**:

- Stacks support _last-in, first-out_ (**LIFO**) order.
- Queues support _first-in, last-out_ (**FIFO**) order.

These structures can be implemented with [arrays](#arrays) or
[linked lists](#linked-lists). They are used less frequently than arrays;
languages may not offer first class support.

**Stack Use Cases**:

- [Call Stacks](https://en.wikipedia.org/wiki/Call_stack)
- Undo/Redo Operations
- Expression Evaluation
- Browser History


**Queue Use Cases**:

- Task Scheduling
- Batch Processing
- Event Handling (Browser)
- Message Buffering
- Web Servers

**Standard Operations:**

| **Operation** | **Time Complexity** |
| -------- | -------- |
| **Push / Enqueue** | **O(1)** |
| **Pop / Dequeue** | **O(1)** |
| **Peek** | **O(1)** |
| **Search** | **O(N)** |