def solution():
    m, n = map(int, input().split())
    a = []
    text = ""
    for i in range(m):
        temp = list(map(int, input().split()))
        a.append(temp)
    for j in range(n):
        for i in range(m):
            if(a[i][j] >= 0):
                break
            if(i == m - 1):
                text += str(j)
                if(j != n - 1):
                    text += " "
    print(text)

solution()