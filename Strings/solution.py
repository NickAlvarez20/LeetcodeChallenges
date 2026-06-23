def add_seconds_to_times(timePoints, seconds):
    res = []
    for item in timePoints:
        time_parts = [int(part) for part in item.split(":")]
        seconds_since_start = (
            time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2] + seconds
        )
        total_seconds = (seconds_since_start) % (24 * 3600)

        hours, remainder = divmod(total_seconds, 3600)
        minutes, second = divmod(remainder, 60)
        res.append(f"{hours:02d}:{minutes:02d}:{second:02d}")
    return res


test = add_seconds_to_times(["10:00:00", "23:30:00"], 3600)
