import math

def isPrime(num):
    if(num < 2):
        return False
    y = int(math.sqrt(num)) + 1
    for x in range(2, y):
        if(num % x == 0):
            return False
    return True

def solution():
    m = int(input())
    n = m
    a = []
    total = 0
    for i in range(m):
        temp = list(map(int, input().split()))
        a.append(temp)
    
    for i in range(m):
        for j in range(n):
            if(j == i and isPrime(a[i][j])):
                total += 1
                
    print(total)
solution()
