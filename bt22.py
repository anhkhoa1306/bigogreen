def yesOrNo():
    n = str(input())
    reversedN = reverseText(n)
    if(n == reversedN):
        print('YES')
    else:
        print('NO')


def reverseText(n):
    rev = ''
    for c in range(len(n), 0, -1):
        rev += n[c -1]
    return rev


yesOrNo()