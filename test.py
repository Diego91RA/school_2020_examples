l = [1, 2, 3, 4, 5]

print(l[1])

print(l[-1])
print(l[1:])

print(l[1:3])

print(l[1:4:2])

s = '1234567890'

print(s[1])
print(s[2:])
print(s[-1])
print(s[2:8:3])

sl = list(s)

print(sl)

for i in s:
    print(i, end='')


l.append(3)
print(l)


s = 'wertwe werwerwwe dfgdfgf dfghdhgfd'
spl = s.split(' ')
print(spl)




lind_ind = [1, 2, 10, 15, 20]

print(lind_ind.index(20))