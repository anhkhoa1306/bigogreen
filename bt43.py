def contain(c, s):
    return s.find(c) >= 0
def solution():
    s = input().upper()
    if(contain('B', s) or contain('I', s) or contain('G', s) or contain('O', s)):
        print('YES')
        return
    print('NO')
solution()