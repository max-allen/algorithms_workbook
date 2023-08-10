# Given a list of existing appointments and an appointment to schedule,
# determine whether the appointment can be scheduled. Appointments must
# be non overlapping.

# [[2, 4], [4, 6]], [0, 1] -> True
# [[2, 4], [4, 6]], [7, 8] -> True
# [[2, 4], [4, 6]], [1, 3] -> False
# [[2, 4], [4, 6]], [5, 6] -> False

# Suppose n1, n2 where n1 < n2. A non overlapping range
# would be given by a k1, k2 s.t. k1 > n2 or k2 < n1. An overlapping
# range is therefore ~(k1 > n2 or k2 < n1) -> k1 <= n2 and k2 >= n1.


def can_schedule(existing, current):
    curr_start, curr_end = current[0], current[1]

    for appt in existing:
        start, end = appt[0], appt[1]

        if curr_start <= end and curr_end >= start:
            return False

    return True
