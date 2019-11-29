def smallestNumber(a):
    min = a[0]
    for x in a:
        if(x < min):
            min = x
    return min

def totalEnergy():
    n = int(input())
    a = list(map(int, input().split()))
    smallestTree = smallestNumber(a)
    totalEnergy = 0
    for x in a:
        if(x > smallestTree):
            totalEnergy += x - smallestTree
    print(totalEnergy)

totalEnergy()