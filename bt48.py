def contain(n, a):
    for x in range(len(a)):
        if(a[x] == n):
            return True
    return False

def solution():
    s = input()
    a = []
    for x in range(len(s)):
        if not contain(s[x], a):
            a.append(s[x])
    print(len(a))

solution()