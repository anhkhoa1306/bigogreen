import math
import sys

def isPrime(p):
    if(p < 2):
        return False
    y = int(math.sqrt(p)) + 1
    for x in range(2, y):
        if(p % x == 0):
            return False
    return True

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    sys.setrecursionlimit(1000000)
    position = recursive(a, 0)
    print(position)

def recursive(a, index):
    if(index == len(a) - 1):
        if(isPrime(a[index])):
            return index
        return -1
    if(isPrime(a[index])):
        return index
    return recursive(a, index + 1)

solution()