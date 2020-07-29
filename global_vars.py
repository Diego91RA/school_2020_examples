a = 10

def func():
    a = 20
    print(id(a))
    print(a)

func()
print(a)
print(id(a))

print()

def func_2():
    global a
    a = 30
    print(a)
    print(id(a))

func_2()
print(a)
print(id(a))
