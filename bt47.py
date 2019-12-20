def totalSlot(n, s):
    ss = s.upper()
    total = 0
    for x in range(len(ss)):
        if(n == ss[x]):
            total += 1
    return total

def isIn(c, a):
    for x in range(len(a)):
        if(a[x] == c):
            return True
    return False

def solution():
    n = int(input())
    a = []
    while(n > 0):        
        s = input()
        smallest = ''
        t = len(s)
        i = 0
        b = []
        for i in range(len(s)):
            if(isIn(s[i], b)):
                continue
            else:
                b.append(s[i])
            c = s[i].upper()
            x = totalSlot(c, s)
            if(x == t):
                if(smallest == '' or c < smallest):
                    smallest = c
                    t = x
            elif(x < t):
                smallest = c
                t = x
        a.append(smallest)
        n -= 1
    for j in range(len(a)):
        print(a[j])
solution()