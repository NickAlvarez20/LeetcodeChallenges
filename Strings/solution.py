def add_days(date, n):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    split_time = date.split("-")
    parsed_dates = [int(chunk) for chunk in split_time]

    curr_year, curr_month, curr_day = parsed_dates[0], parsed_dates[1], parsed_dates[2]
    total_days = curr_day + n

    while True:
        # 1. Determine leap year helper func
        is_leap = (curr_year % 4 == 0 and curr_year % 100 != 0) or curr_year % 400 == 0
        # 2. check month and update max_days
        if curr_month == 2 and is_leap:
            max_days = 29
        else:
            max_days = days_in_month[curr_month]

        # 3. do total days fit?
        if total_days <= max_days:
            break # we've determined the last month
        else:
            total_days -= max_days
            curr_month += 1

        # 4. Check if year is december
        if curr_month > 12:
            curr_month = 1
            curr_year += 1

    return f"{curr_year}-{curr_month:02d}-{total_days:02d}"


print(add_days("2004-01-01", 365))












# split_time = date.split("-")
# int_date = [int(chunk) for chunk in split_time]

# # Tracking variables
# curr_year = int_date[0]
# curr_month = int_date[1]
# total_days = int_date[2] + n

# while True:
#     # 1. Figure out how many days are in the current month
#     # (This handles the annoying leap year math automatically)
#     is_leap = (curr_year % 4 == 0 and curr_year % 100 != 0) or curr_year % 400 == 0
#     if curr_month == 2 and is_leap:
#         max_days = 29
#     else:
#         max_days = days_in_month[curr_month]

#     # 2. Check if our remaining days fit in this month
#     if total_days <= max_days:
#         break  # We've found the final day! Stop looping.

#     # 3. If they don't fit, jump to the next month
#     total_days -= max_days
#     curr_month += 1

#     # 4. If we go past December, reset to January and advance the year
#     if curr_month > 12:
#         curr_month = 1
#         curr_year += 1

# return f"{curr_year}-{curr_month:02d}-{total_days:02d}"
