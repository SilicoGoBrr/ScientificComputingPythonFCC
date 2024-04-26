def add_time(start, duration, day_week=None):
    # Splitting start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Splitting duration
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Converting PM time to 24-hour format
    if period == 'PM':
        start_hour += 12

    # Adding duration
    new_minute = (start_minute + dur_minute) % 60
    carry_hour = (start_minute + dur_minute) // 60
    new_hour = (start_hour + dur_hour + carry_hour) % 24
    days_later = (start_hour + dur_hour + carry_hour) // 24

    # Calculating new period
    new_period = "AM" if new_hour < 12 else "PM"
    if new_hour >= 12:
        new_hour %= 12
    if new_hour == 0:
        new_hour = 12

    # Calculating the day of the week
    day_offset = 0
    if day_week:
        day_week = day_week.capitalize()
        day_offset = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday').index(day_week)
    
    new_day_offset = (day_offset + days_later) % 7
    new_day = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')[new_day_offset]

    # Compose the new time string
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"
    if day_week:
        new_time += f", {new_day}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time
