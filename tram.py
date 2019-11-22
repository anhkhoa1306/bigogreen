def tram():
    t = int(input())
    total = 0
    max = 0
    while(t >= 1):
        i, o = map(int, input().split())
        total = total - i + o
        if(total > max):
             max = total
        t -= 1
    print(max)
tram()