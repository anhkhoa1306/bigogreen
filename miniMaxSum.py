import sys
def solution():
    ar = list(map(int, input().split()))
    sys.setrecursionlimit(1000000)
    maxIndex = maxIndexRecursive(ar, 0, 1)
    minIndex = minIndexRecursive(ar, 0, 1)
    minTotal = sumRecursive(ar, 0, maxIndex)
    maxTotal = sumRecursive(ar, 0, minIndex)
    print("{0} {1}".format(minTotal, maxTotal))

def maxIndexRecursive(ar, i, j):
    if(j == len(ar) - 1):
        if(ar[j] > ar[i]):
            return j
        else:
            return i
    if(ar[j] > ar[i]):
        i = j
    return maxIndexRecursive(ar, i, j + 1)

def minIndexRecursive(ar, i, j):
    if(j == len(ar) - 1):
        if(ar[j] < ar[i]):
            return j
        else:
            return i
    if(ar[j] < ar[i]):
        i = j
    return minIndexRecursive(ar, i, j + 1)

def sumRecursive(ar, index, excludeIndex):
    if(index == len(ar) - 1):
        if(index == excludeIndex):
            return 0
        else:
            return ar[index]
    if(index == excludeIndex):
        return 0 + sumRecursive(ar, index + 1, excludeIndex)
    return ar[index] + sumRecursive(ar, index + 1, excludeIndex)

solution()