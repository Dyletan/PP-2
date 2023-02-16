import datetime
def minusFiveDays(date):
    return date - datetime.timedelta(days = 5)
date = datetime.datetime.now()
print(minusFiveDays(date))