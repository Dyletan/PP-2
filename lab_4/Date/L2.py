import datetime
def threeDays():
    date = datetime.datetime.today()
    delta = datetime.timedelta(days = 1)
    print("Yesterday:", (date - delta).strftime("It is the %d of %B and the year is %Y"))
    print("Today:", (date).strftime("It is the %d of %B and the year is %Y"))
    print("Tomorrow:", (date + delta).strftime("It is the %d of %B and the year is %Y"))
threeDays()