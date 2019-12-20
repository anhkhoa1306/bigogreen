def isMaxInArray(m, a):
    for x in a:
        if(x > m):
            return False
    return True

def isMinInArray(j, i, a):
    min = a[i][j]
    l = len(a) - 1
    while(l >= 0):
        if(a[l][j] < min):
            return False
        l -= 1
    return True

def solution():
    m, n = map(int, input().split())
    a = []

    total = 0
    for x in range(m):
        temp = list(map(int, input().split()))
        a.append(temp)

    for i in range(m):
        for j in range (n):
            if not isMinInArray(j, i, a):
                continue
            elif(isMaxInArray(a[i][j], a[i])):
                total += 1
    print(total)
solution()
    

