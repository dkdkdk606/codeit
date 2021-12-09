import os, math, random, datetime

print(os.getlogin())
print(random.random(),random.random(),random.random(),random.random())

# print(m.atan(1))
pi_day = datetime.datetime(2020, 3, 14, 13, 42, 59, 90)
print(pi_day)
print(type(pi_day))
daydelta = datetime.timedelta(days=10, minutes=10)

print(pi_day+ daydelta)
print(daydelta.days)
print(pi_day.year)
today = datetime.datetime.now()

print(today.strftime("%a, %b %dth %Y 1년중 %j번쨰 날"))
