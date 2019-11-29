def yesOrNo():
    n = int(input())
    a = list(map(int, input().split()))
    yes = True
    for x in a:
        if(x == 0):
            yes = False
            break
    if(yes):
        print('YES')
    else:
        print('NO')

yesOrNo()