def maxInRow(n, a):
    for x in a:
        if(x > n):
            return False
    return True

def maxInColumn(n, j, a):
    l = len(a) - 1
    while(l >= 0):
        if(a[l][j] > n):
            return False
        l -= 1
    return True

def maxInOtherDiagonals(n, j, a):
    leftRow = j
    rightRow = len(a) - leftRow - 1
    t = 0
    while(leftRow >= 0):
        if(a[leftRow][t] > n):
            return False
        leftRow -= 1
        t += 1
    
    r = len(a) - 1
    while(rightRow >= 0):
        if(a[rightRow][r] > n):
            return False
        rightRow -= 1
        r -= 1
    return True

def solution():
    m = int(input())
    a = []
    for i in range(m):
        temp = list(map(int, input().split()))
        a.append(temp)
    total = 0
    for i in range(m):
        for j in range(m):
            n = a[i][j]
            if(maxInRow(n, a[i]) and maxInColumn(n, j, a)):
                if(j == 0 or j == m - 1):
                    if(maxInOtherDiagonals(n, j, a)):
                        total += 1
                else:
                    total += 1

    print(total)
solution()