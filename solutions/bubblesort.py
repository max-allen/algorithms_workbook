# O(N^2) Time Complexity | O(1) Space Complexity


def bubblesort(unsorted_elements):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for idx in range(len(unsorted_elements) - 1):
            nxt_idx = idx + 1
            curr = unsorted_elements[idx]
            nxt = unsorted_elements[nxt_idx]

            if nxt < curr:
                is_sorted = False
                unsorted_elements[idx] = nxt
                unsorted_elements[nxt_idx] = curr

    return unsorted_elements
