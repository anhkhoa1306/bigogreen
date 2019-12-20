def isArrayValid(a):
    i = 1
    while(i <= 9):
        if not contain(i, a):
            return False
        i += 1
    return True


def contain(i, a):
    for x in range(len(a)):
        if(a[x] == i):
            return True
    return False

def isValid(a, b, c):
    i = 1
    while(i <= 9):
        if not contain(i, a) or not contain(i, b) or not contain(i, c):
            return False
        i += 1
    return True

def solution():
    m = 9
    n = 9
    a = []
    b = []
    c = []
    d = []
    while(m > 0):
        temp = list(map(int, input().split()))
        if not isArrayValid(temp):
            print('NO')
            return
        d.append(temp)
        for i in range(len(temp)):
            if(i >= 0 and i < 3):
                a.append(temp[i])
            elif(i >= 3 and i < 6):
                b.append(temp[i])
            else:
                c.append(temp[i])
        if(len(a) == 9 and len(b) == 9 and len(c) == 9):
            if not isValid(a, b, c):
                print('NO')
                return
            a = []
            b = []
            c = []
        m -= 1

    z = []
    for j in range(n):
        for i in range(n):
            z.append(d[i][j])
        if not isArrayValid(z):
            print('NO')
            return
        z = []

    print('YES')
solution()

