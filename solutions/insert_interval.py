def insert_interval(existing_intervals, new_interval):
    result = []

    for idx in range(len(existing_intervals)):
        interval = existing_intervals[idx]

        # new interval occurs before
        if new_interval[1] < interval[0]:
            result.append(new_interval)
            return result + existing_intervals[idx:]

        # new interval occurs after
        elif new_interval[0] > interval[1]:
            result.append(interval)

        else:
            new_interval = [
                min(new_interval[0], interval[0]),
                max(new_interval[1], interval[1]),
            ]

    result.append(new_interval)
    return result
