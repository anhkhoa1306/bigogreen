class Score:
    def __init__(self, c, s):
        self.c = c
        self.s = s
    
    def display(self):
        print(int(self.c))

def merge(l, r, a):
    i = 0
    j = 0
    k = 0
    ll = len(l)
    lr = len(r)

    while(i < ll and j < lr):
        if(l[i].s > r[j].s):
            a[k] = l[i]
            i += 1
        elif(l[i].s < r[j].s):
            a[k] = r[j]
            j += 1
        else:
            if(l[i].c < r[j].c):
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
        k += 1
    
    while(i < ll):
        a[k] = l[i]
        k += 1
        i += 1

    while(j < lr):
        a[k] = r[j]
        k += 1
        j +=1

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
    n, k = map(int, input().split())
    a = []
    while(n > 0):
        c, s = map(float, input().split())
        sc = Score(c, s)
        a.append(sc)
        n -= 1
    mergeSort(a, len(a))

    for x in range(len(a)):
        if(x == k):
            break
        else:
            a[x].display()

solution()