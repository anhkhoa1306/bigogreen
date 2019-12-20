def merge(l, r, a):
    i = 0
    j = 0
    k = 0
    ll = len(l)
    lr = len(r)
    while(i < ll and j < lr):
        if(l[i] > r[j]):
            a[k] = r[j]
            j +=1
        else:
            a[k] = l[i]
            i += 1
        k += 1
    
    while(i < ll):
        a[k] = l[i]
        i += 1
        k += 1
    while(j < lr):
        a[k] = r[j]
        j += 1
        k += 1

def mergeSort(a, n):
    if(n == 1):
        return a
    nL = n // 2
    nR = n - nL

    L = a[0:nL]
    R = a[nL:n]

    mergeSort(L, nL)
    mergeSort(R, nR)
    merge(L, R, a)

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    mergeSort(a, n)
    if(n % 2 != 0):
        print(a[int(n/2)])
    else:
        x = n // 2
        y = x - 1
        print((a[x] + a[y])/2)

solution()