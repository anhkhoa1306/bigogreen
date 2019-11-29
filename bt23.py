def totalLike():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for l in a:
        total += l
    print(total)
totalLike()