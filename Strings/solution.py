import math

def time_period_length(time_period):
    times = time_period.split("-")
    cleansed_times = []
    time_in_seconds = []
    for time in times:
        parsed_time = time.strip()
        cleansed_times.append(parsed_time)

    for item in cleansed_times:
        time_parts = [int(part) for part in item.split(":")]
        seconds_since_start = time_parts[0] * 60 + time_parts[1]
        time_in_seconds.append(seconds_since_start)

    difference_in_seconds = time_in_seconds[1] - time_in_seconds[0]

    return difference_in_seconds

print(time_period_length("12:15:30 - 14:00:00"))
