# f = open('test.txt','w')
#
# f.write('qweqrete\n')
# f.write('qwrqrqwr\n')
# f.write('eryrthfghg\n')
#
# f.close()
#
# f = open('test.txt','r')
#
# # print(f.read())
# #
# # for line in f:
# #     print(line)
#
# f.close()
#
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line)
#     try:
#         f.write('qwerewr')
#     except Exception as e:
#         pass


import csv
import time
from datetime import datetime

# rows = [['1', '2', '3'], ['4', '5', '6']]
# with open('my.csv', 'w+', newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     for row in rows:
#         writer.writerow(row)

# with open('my.csv', 'r+', newline='') as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     for row in reader:
#         print(row)

with open('time_test.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')

    for i in range(10):
        time_now = datetime.now()
        row = [time_now, i]
        writer.writerow(row)

        time.sleep(1)



while 1:

    row = {}

    rr = client.read_input_registers(0, 10, unit=1)
    print(rr.registers)
    with open(csv_name, 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n')


        row['temperature'] = rr.registers[0] / 100

        writer.writerow(row)
    time.sleep(1)