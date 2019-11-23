import math
import numbers

def pair():
    n, m = map(int, input().split())
    origin = n
    total = 0
    while(n >= 0):
        if(perfectSqrt(n)):
            a = math.sqrt(n)
            b = origin - a * a
            if(a + b*b == m):
                total += 1
        n -= 1
    print(total)

def perfectSqrt(n):
    r = math.sqrt(n)
    return (r - int(r)) == 0

pair()