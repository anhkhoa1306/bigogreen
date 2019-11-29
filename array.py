def solution():
    n = int(input())
    a = list(map(int, input().split()))
    first = []
    second = []
    third = []
    for x in a:
        if(x < 0):
            first.append(x)
        elif(x > 0):
            second.append(x)
        else:
            third.append(x)

    if(len(second) == 0):
        second, first = swapArray(first)

    if(len(first) % 2 == 0):
        first, third = moveItem(first, third)

    f = str(len(first))
    s = str(len(second))
    t = str(len(third))

    for n in first:
        f += ' ' + str(n)
    for n in second:
        s += ' ' + str(n)
    for n in third:
        t += ' ' + str(n)
        
    print(f)
    print(s)
    print(t)

def swapArray(b):
    c = []
    d = []
    for y in range(0, 2):
        c.append(b[y])
    for x in range(2, len(b)):
        d.append(b[x])
    return c, d

def moveItem(a, b):
    x = a[0]
    b.append(x)
    c = []
    for y in a:
        if(y != x):
            c.append(y)
    return c, b

solution()