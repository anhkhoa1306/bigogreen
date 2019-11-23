def removeZero(number):
    if(number == 0):
        return 0
    else:
        return int(str(number).replace("0", ""))

def yesOrNo():
    a = int(input())
    b = int(input())
    aWithoutZero = removeZero(a)
    bWithoutZero = removeZero(b)
    c = a + b
    cWithoutZero = removeZero(c)
    d = aWithoutZero + bWithoutZero
    if(d == cWithoutZero):
        print('YES')
    else:
        print('NO')

yesOrNo()