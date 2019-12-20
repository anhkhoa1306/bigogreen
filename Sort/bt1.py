def insertAsc(a, i, x):
    while(i > 0):
        if(a[i - 1] > x):
            t = a[i - 1]
            a[i] = t
            a[i - 1] = x
        i -= 1
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    if(n == 1):
        print(a[0])
        return
    m = 1
    while(m < n):
        x = a[m]
        insertAsc(a, m, x)
        m += 1
    for y in range(len(a)):
        if(y == len(a) - 1):
            print(a[y])
        else:
            print(a[y], end = " ")

solution()