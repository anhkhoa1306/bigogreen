import math
def isPrime(n):
    if(n < 2):
        return False
    if(n == 2):
        return True
    p = int(math.sqrt(n)) + 1
    for z in range(2, p):
        if(n % z == 0):
            return False
    return True

def insertAsc(a, i, x):
    j = i
    while(i > 0):
        if not isPrime(a[i - 1]):
            t = a[i - 1]
            if(t > x):
                a[j] = t
                a[i - 1] = x
                j = i - 1
        i -= 1
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    if(n == 1):
        print(a[0])
        return
    m = 1
    while(m < n):
        x = a[m]
        if(isPrime(x)):
            m += 1
            continue
        insertAsc(a, m, x)
        m += 1
    for y in range(len(a)):
        if(y == len(a) - 1):
            print(a[y])
        else:
            print(a[y], end = " ")

solution()