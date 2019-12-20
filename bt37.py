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
    product = 1
    a = []
    for i in range(m):
        temp = list(map(int, input().split()))
        a.append(temp)
    x = 0
    while(x < m):
        y = m - x - 1
        if(isPrime(a[x][y])):
            product = (product * a[x][y]) % 1000003
        x += 1
    print(product)

solution()