def merge(l, nL, r, nR, a, n):
    i = 0
    j = 0
    k = 0
    while(i < len(l) and j < len(r)):
        if(l[i] > r[j]):
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1

    while(i < len(l)):
        a[k] = l[i]
        k += 1
        i += 1
    
    while(j < len(r)):
        a[k] = r[j]
        k += 1
        j += 1

def mergeSort(arr, n):
    if(n <= 1):
        return arr
    nL = n // 2
    nR = n - nL
    l = arr[0:nL]
    r = arr[nL:n]

    mergeSort(l, nL)
    mergeSort(r, nR)
    merge(l, nL, r, nR, arr, n)

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    if(n == 1):
        print(a[0])
        return
    mergeSort(a, n)
    for m in range(len(a)):
        if(m == len(a) - 1):
            print(a[m])
        else:
            print(a[m], end = " ")

solution()