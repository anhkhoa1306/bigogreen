def isNumber(c):
    a = ord(c)
    return a >= ord('0') and a <= ord('9')

def solution():
    s = input()
    total = 0
    for i in range(len(s)):
        if(isNumber(s[i])):
            total += 1
    print(total)

solution()