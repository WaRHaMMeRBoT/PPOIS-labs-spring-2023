def to_date(str_date):
    months_lenghts = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    date = str_date.split(' ')
    if len(date) != 2: return None
    date = date[0].split('.') + date[1].split(':')
    for t in date:
        if not(t.isdigit()): return None
    date = [int(el) for el in date]
    if len(date) != 4:
        return None
    if date[1] < 0 or date[1] > 12:
        return None
    if date[0] < 0 or date[0] > months_lenghts[date[1]]:
        return None
    if date[2] < 0 or date[2] > 23:
        return None
    if date[3] < 0 or date[3] > 59:
        return None
    return date

def compare(date1, date2):
    date1 = [date1[1], date1[0], date1[2], date1[3]]
    date2 = [date2[1], date2[0], date2[2], date2[3]]
    for i in range(len(date1)):
        if date1[i] > date2[i]:
            return 'later'
        elif date1[i] < date2[i]:
            return 'earlier'
    return 'same'

def time_of_travel(departure, arrival):
    months_lenghts = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    minutes = arrival[3] - departure[3]
    if minutes < 0:
        minutes += 60
        arrival[2] -= 1
    hours = arrival[2] - departure[2]
    if hours < 0:
        hours += 24
        arrival[0] -= 1
    days = arrival[0] - departure[0]
    if days < 0:
        days += months_lenghts[departure[1]]
        arrival[1] -= 1
    months = arrival[1] - departure[1]
    if months < 0:
        months += 12
    return [months, days, hours, minutes]

def from_time_to_string(time):
    str_time = ''
    periods = ['month', 'day', 'hour', 'minute']
    for i in range(len(time)):
        if time[i] != 0:
            str_time += str(time[i]) + ' ' + periods[i]
            if time[i] != 1: str_time += 's '
            else: str_time += ' '
    return str_time

def from_string_to_time(str_time):
    periods = {'months':0, 'days':1, 'hours':2, 'minutes':3}
    time = [0, 0, 0, 0]
    timelist = str_time.split(' ')
    while len(timelist) > 1:
        period = timelist[1]
        if period[-1] != 's': period += 's'
        if period != 'months' and period != 'days' and period != 'hours' and period != 'minutes':
            return None
        time[periods[period]] = int(timelist[0])
        timelist.pop(0)
        timelist.pop(0)
    return time



    