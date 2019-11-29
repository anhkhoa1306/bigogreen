def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    kScore = a[k -1]
    total = 0
    for x in a:
        if(x > 0 and x >= kScore):
            total += 1
    print(total)

solution()