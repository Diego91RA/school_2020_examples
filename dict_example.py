dic = {'key': 1, 'key2': '1342', 'key3': ["qwqweqw"], 'key4': {'1': 2}}


a= [[1,2,3],[4,5,6],[7,8,9]]

# for key, value in dic.items():
#     print(key, value)
#
# print()
dic['new_key'] = 'new_val'

# for key, value in dic.items():
#     print(key, value)


if 'key' not in dic.keys():
    print('Yes')
else:
    print('No')

arr = [1,6,8,9,3,67,89,235]
print(sorted(arr))
print(list(reversed(arr)))

new_arr = [1,2,3,4, -10, -20, 'qweqwr', 'dfgdrt', [1,2,3]]

import math

for i in new_arr:
    try:
        print(math.sqrt(i))
    except:
        print(i)
    finally:
        print('new item')