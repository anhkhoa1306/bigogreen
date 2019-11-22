def power(n):
    return n*n

def totalPower():
    n = int(input())
    total = 0
    while(n > 0):
        total += power(n)
        n -= 1
    print(total)

totalPower()