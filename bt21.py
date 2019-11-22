import math

def isPrime(p):
    y = int(math.sqrt(p)) + 1
    for x in range(2, y):
        if(p % x == 0):
            return False
    return True

def nearestPrime():
    n = int(input())
    m = n
    origin = n
    first = 0
    second = 0
    
    while(n >= 2):
        if(isPrime(n)):
            first = n
            break
        n -= 1
    
    while(1 == 1):
        if(isPrime(m)):
            second = m
            break
        m += 1
    
    if(origin - first > second - origin):
        print(second)
        return
    print(first)

nearestPrime()