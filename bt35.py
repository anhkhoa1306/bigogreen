import math

def isPrime(num):
    if(num < 2):
        return False
    y = int(math.sqrt(num)) + 1
    for x in range(2, y):
        if(num % x == 0):
            return False
    return True

def contains(num, a):
    for x in a:
        if(x == num):
            return True
    return False

def solution():
    m, n = map(int, input().split())
    a = []
    checked = []
    total = 0
    for i in range(m):
        temp = list(map(int, input().split()))
        a.append(temp)
    for i in range(m):
        if(i == 0 or i == m -1):
            for j in range(n):
                if(isPrime(a[i][j])):
                    total += 1
                    if((i == 0 or i == m - 1) and (j == 0 or j == n - 1)):
                        checked.append(a[i][j])
    
    for j in range(n):
        if(j == 0 or j == n - 1):
            for i in range(m):
                if(i == 0 or i == m - 1 and contains(a[i][j], checked)):
                    continue
                if(isPrime(a[i][j])):
                    total += 1


    print(total)

solution()