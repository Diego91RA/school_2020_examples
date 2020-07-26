l = []
for i in range(2020, 10001):
    if i % 4 == 0:
        if i % 400 == 0:
            l.append(i)
        elif i % 100 == 0:
            pass
        else:
            l.append(i)
print(l)
print(len(l))

c = 0
import calendar
for i in range(2020, 10001):
    if calendar.isleap(i):
        c += 1
print(c)