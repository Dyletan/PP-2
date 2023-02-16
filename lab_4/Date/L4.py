import datetime
def diff(date1, date2):
    delta = date1 - date2
    return delta.total_seconds()
date1 = datetime.datetime.now()
date2 = datetime.datetime(2023, 1, 30, 10, 45)
print(diff(date1, date2))