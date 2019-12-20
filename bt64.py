import sys
def solution():
    n, m = map(int, input().split())
    sys.setrecursionlimit(1000000)
    r = 0
    if(n > m):
        r = recursive(m, n%m)
    else:
        r = recursive(n, m%n)
    print(r)

def recursive(n, m):
    if(m == 0):
        return n
    return recursive(m, n%m)
solution()