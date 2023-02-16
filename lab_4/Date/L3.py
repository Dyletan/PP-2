import datetime
def removeMicro(date):
    return date.strftime("%d-%m-%Y %H:%M:%S")
date = datetime.datetime.now()
print(removeMicro(date))