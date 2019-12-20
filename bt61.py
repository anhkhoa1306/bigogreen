import sys
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    sys.setrecursionlimit(1000000)
    total = recursive(a, 0)
    print(total)

def recursive(a, index):
    if(index == len(a) - 1):
        x = a[index]
        if(x % 2 == 0):
            return x
        else:
            return 0
    if(a[index] % 2 == 0):
        return a[index] + recursive(a, index + 1)
    else:
        return 0 + recursive(a, index + 1)

solution()