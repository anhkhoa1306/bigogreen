def maxNumber(a):
    max = 1
    for x in a:
        if(x > max):
            max = x
    return max

def smallestMissingNumber():
    n = int(input())
    a = list(map(int, input().split()))
    max = maxNumber(a)
    index = 1
    while(index <= max):
        counter = 0
        for x in a:
            if(x != index):
                counter += 1
        if(counter == n):
            break
        index += 1
    print(index)

smallestMissingNumber()