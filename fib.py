fib = []

for i in range(200):
    if i < 2:
        fib.append(i)
    else:
        f = fib[i - 1] + fib[i - 2]
        fib.append(f)

print(fib)


# for f in fib

# for i in range(len(fib)):
#     print(fib[i])


for i, f in enumerate(fib):
    s = 0
    l = list(str(f))
    for k in l:
        s += int(k)
    print(i, s)
