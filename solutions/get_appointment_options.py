# Write an algorithm that accepts two calendars, two bounds, and a meeting duration.
# Return meetings that can be scheduled from the input.


# traverse arrays

# at each index, determine latest party
# if either has a next start time <= duration + current_end
# -> move on

# check opposite party for start time duration + current end away


# Sample Input:

[["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]

["9:00", "20:00"]

[["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]

["10:00", "18:30"]

30

# Sample Output:

[["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]


cals = [
    [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]],
    [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]],
]


def get_appointment_options(calendars):
    cal_one, cal_two = calendars[0], calendars[1]

    for idx in range(len(cal_one)):
        event_one, event_two = cal_one[idx], cal_two[idx]

        start_one, end_one = event_one[0], event_one[1]
        start_two, end_two = event_two[0], event_two[1]

        latest_end = end_one if end_one > end_two else end_two
