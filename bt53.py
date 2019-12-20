def solution():
    m = int(input())
    a = []
    for x in range(m):
        a.append(int(input()))
    total = 0
    previous = 0
    for y in range(len(a)):
        if(a[y] != previous):
            total += 1
        previous = a[y]
    print(total)

solution()
    
