import sys
def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sys.setrecursionlimit(1000000)
    total = 0
    c = 0
    while(c < n - 1):
        total += recursive(a, c, c + 1, k)
        c +=1
    print(total)

def recursive(ar, index, nextIndex, k):
    if(index == len(ar) - 1):
        return 0
    if(nextIndex == len(ar) - 1):
        if((ar[index] + ar[nextIndex]) % k == 0):
            return 1
        else:
            return 0
    if((ar[index] + ar[nextIndex]) % k == 0):
        return 1 + recursive(ar, index, nextIndex + 1, k)
    else:
        return 0 + recursive(ar, index, nextIndex + 1, k)

solution()