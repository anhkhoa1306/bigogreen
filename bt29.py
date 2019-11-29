def isEven(n):
    if(n % 2 == 0):
        return True
    else:
        return False

def yesOrNo():
    n = int(input())
    a = list(map(int, input().split()))
    if not isEven(n):
        print('NO')
        return
    totalZero = 0

    for x in a:
        if(x == 0):
            totalZero += 1

    if(n / totalZero == 2):
        print('YES')
    else:
        print('NO')

yesOrNo()