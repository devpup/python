#-*- coding: utf-8 -*-
import datetime

#datetime file에 datetime class
now = datetime.datetime.now()

print(type(now))
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

print(now.strftime('%Y-%m-%d %H:%M:%S'))
#print(now.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*u"년월이시분초".encode('euc-kr')))

print(now + datetime.timedelta(weeks=1)) #days, hours, minutes, seconds

print(now.replace(year = (now.year + 1)))