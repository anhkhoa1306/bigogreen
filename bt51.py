def isOverTwelve(n):
    return n >= 12

def solution():
    k = int(input())
    isBonusApplied = isOverTwelve(k)
    total = 15000
    if(k < 2):
        print(total)
        return
    k = k - 1
    if(k <= 4):
        total += (k * 13500)
        print(total)
        return
    total += (4 * 13500)
    k = k - 4
    total += (k * 11000)
    if(isBonusApplied):
        total -= (total * 0.1)
    print(int(total))

solution()