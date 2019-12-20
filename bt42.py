def solution():
    m, n = map(int, input().split())
    a, b, p = map(int, input().split())
    first = 0
    second = 0
    third = 0
    for i in range(m):
        for j in range(n):
            if(i == 0):
                if(j == 0):
                    print(a, end= " ")
                    first = a
                    continue
                elif(j == 1):
                    print(b, end= " ")
                    second = b
                    continue
            third = int((first + second) % p)
            if(j == n - 1):
                print(third)
            else:
                print(third, end= " ")
            first = second
            second = third
    
solution()