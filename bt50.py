def solution():
    s = input()
    a = []
    t = ""
    for x in range(len(s)):
        if(x == len(s) - 1):
            t += s[x]
            a.append(t)
        elif(s[x] == ' '):   
            a.append(t)
            t = ""
        else:
            t += s[x]
    l = len(a) - 1
    while(l >= 0):
        if(l > 0):
            print(a[l], end=" ")
        else:
            print(a[l])
        l -= 1
solution()