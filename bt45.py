def solution():
    s = input()
    ans = ""
    a = []
    previousChar = ""
    for i in range(len(s)):
        if(s[i] !=' '):
            ans += s[i]
            if(i == len(s) - 1):
                a.append(ans)
        elif(s[i] == ' '):
            if(len(ans) > 0):
                if(previousChar != ' '):
                    a.append(ans)
                    ans = ""
        previousChar = s[i]
    
    for x in range(len(a)):
        if(x == len(a) - 1):
            print(a[x])
        else:
            print(a[x], end = " ")

solution()