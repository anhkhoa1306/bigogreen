def solution():
    m, n = map(int, input().split())
    total = 0
    for i in range(m):
        temp = list(map(int, input().split()))
        for x in temp:
            if(x > 100):
                total += 1
                
    print(total)
solution()