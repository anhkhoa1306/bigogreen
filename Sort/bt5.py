def isEven(n):
    return n % 2 == 0
def insertAscEven(a, i, x):
    index = i
    while(i > 0):
        t = a[i - 1]
        if(isEven(t) and t > x):
            a[i - 1] = x
            a[index] = t
            index = i - 1
        i -= 1
def insertAscOdd(a, i, x):
    index = i
    while(i > 0):
        t = a[i - 1]
        if(not isEven(t) and t < x):
            a[i - 1] = x
            a[index] = t
            index = i - 1
        i -= 1

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    if(len(a) == 1):
        print(a[0])
        return
    m = 1
    while(m < n):
        x = a[m]
        if(isEven(x)):
            insertAscEven(a, m, x)
        else:
            insertAscOdd(a, m, x)
        m += 1
    for y in range(len(a)):
        if(y == len(a) - 1):
            print(a[y])
        else:
            print(a[y], end = " ")

solution()


    
