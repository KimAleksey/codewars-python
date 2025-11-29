"""
https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e/python
"""

def get_day(day, is_leap):
    if is_leap:
        days_in_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    interval_days = [0]
    for days in days_in_year:
        interval_days.append(days + interval_days[-1])
    month = 0
    for i in range(len(interval_days)-1):
        if interval_days[i] <= day <= interval_days[i+1]:
            month = i + 1
            break
    return f"{months[month-1]}, {day - sum(days_in_year[:month-1])}"


print(get_day(366, 1))