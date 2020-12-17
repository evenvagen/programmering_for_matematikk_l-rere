def overtime(hours, hourly_rate):
    if hours <= 37.5:
        pay = hours * hourly_rate
    else:
        pay = 37.5 * hourly_rate + (hours - 37.5) * hourly_rate * 1.5
    return pay


print(overtime(10, 300))
