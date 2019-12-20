def solution():
    s = input()
    flag = False
    previous = ''
    a = ""
    for x in range(len(s)):
        if(s[x] == '.'):
            flag = True
            previous = s[x]
            a += s[x]
            continue
        elif(flag and previous == ' '):
            previous = s[x]
            a += s[x].upper()
            flag = False
            continue
        elif(flag and s[x] != ' '):
            flag = False
        a += s[x]    
        previous = s[x]
    print(a)
solution()        