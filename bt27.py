import math
def isPrime(n):
    s = int(math.sqrt(n)) + 1
    for x in range(2, s):
        if(n % x == 0):
            return False
    return True

def totalPrime():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for x in a:
        if(x >= 2 and isPrime(x)):
            total += 1
    print(total)

totalPrime()