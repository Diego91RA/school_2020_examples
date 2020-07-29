import matplotlib.pyplot as plt
import csv
from datetime import datetime

x = []
y = []


with open('1595937232.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        element = row[0]
        new_time, temp = element.split(';')
        # print(new_time, temp)

        x.append(new_time)
        y.append(float(temp))

# print(x)
# print(y)

date_obj = datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S.%f')
# print(date_obj)
# print(type(date_obj))

print(date_obj.strftime('%d.%m.%Y %H:%M:%S'))

x_new = []
for elem in x:
    date_obj = datetime.strptime(elem, '%Y-%m-%d %H:%M:%S.%f')
    x_new.append(date_obj.strftime('%d.%m %H:%M'))


fig, ax = plt.subplots()
plt.grid(True)
ax.plot(x_new, y, color='blue', linewidth=2)

ax.xaxis.set_major_locator(plt.MaxNLocator(10))
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(12)


# plt.savefig("sample.png", dpi=300)

plt.show()
