import math
def isPrime(p):
    y = int(math.sqrt(p)) + 1
    for x in range(2, y):
        if(p % x == 0):
            return False
    return True

def totalPrime():
    n = int(input())
    total = 0
    for i in range(2, n, 1):
        if(isPrime(i)):
            total += i
    print(total)

totalPrime()