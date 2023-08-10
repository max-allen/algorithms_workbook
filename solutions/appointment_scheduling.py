appt_one = {"start_time": 3, "end_time": 10}
appt_two = {"start_time": 13, "end_time": 20}
appts = [appt_one, appt_two]


# def schedule_appointments(existing, new):
#     for appt in existing:
#         # appointment is after existing appts
#         if appt["start_time"] <= new["start_time"]:
#             if appt["end_time"] > new["start_time"]:
#                 return False

#         # appointment is before existing appts
#         else:
#             if appt["start_time"] < new["end_time"]:
#                 return False

#     return True


def schedule_appointments(existing, new):
    appts_hash = {}

    for appt in existing:
        curr = appt["start_time"]
        end_time = appt["end_time"]

        while curr < end_time:
            appts_hash[curr] = True
            curr += 1

    curr = appt["start_time"]

    while curr < appt["end_time"]:
        if appts_hash[curr]:
            return False
        curr += 1

    return True


result = schedule_appointments(appts, {"start_time": 2, "end_time": 13})
