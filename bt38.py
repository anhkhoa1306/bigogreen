def totalEven(a):
    total = 0
    for x in a:
        if(x % 2 == 0):
            total += 1
    return total

def solution():
    m, n = map(int, input().split())
    
    min = m - 1

    previous = 0

    total = 0

    for x in range(m):
        temp = list(map(int, input().split()))
        total = totalEven(temp)
        if(total > previous):
            previous = total
            min = x
        elif(total == previous):
            if(min > x):
                min = x
    print(min)

solution()
        
