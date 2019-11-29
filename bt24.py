def maxLike():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for l in a:
        if(l > max):
            max = l
    print(max)
maxLike()