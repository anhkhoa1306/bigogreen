def toUpper(c):
    return c.upper()

def toLower(c):
    return c.lower()

def solution():
    n = int(input())
    previousChar = ''
    a = []
    while(n > 0):
        name = ""
        s = input()
        for x in range(len(s)):
            if(x == 0 or previousChar == ' '):
                name += toUpper(s[x])
            else:
                name += toLower(s[x])
            previousChar = s[x]
        n -= 1
        a.append(name)
    for n in a:
        print(n)
solution()
            