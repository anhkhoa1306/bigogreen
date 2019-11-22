def smallestMod(a, b):
    if(a % b == 0):
        return b
    if(b % a == 0):
        return a
    diff = 0
    if(a > b):
        diff = a - b
    else:
        diff = b - a
    while(diff >= 2):
        if(a % diff == 0 and b % diff == 0):
            return diff
        diff -= 1
    return diff

def reduce():
    a, b = map(int, input().split())
    s = smallestMod(a, b)
    x = a
    y = b
    if(a % s == 0):
        x = a / s
    if(b % s == 0):
        y = b / s
    print('{0} {1}'.format(int(x) ,int(y)))

reduce()