# Given two non empty arrays of integers, determine whether the subsequence

# [1, 2, 3, 4], [1, 3, 4] -> True

# [5, 6, 7, 8, 9], [9, 8] -> False


def is_subsequence(array, sequence):
    seq_idx = 0

    for el in array:
        if seq_idx < len(sequence):
            seq_el = sequence[seq_idx]
        if el == seq_el:
            seq_idx += 1

    return seq_idx == len(sequence)
