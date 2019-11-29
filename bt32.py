def yesOrNo():
    n = int(input())
    a = list(map(int, input().split()))
    if(a[n-1] == 0):
        print('NO')
        return
    
    flag = False
    counterComputer = 0
    for x in a:
        if(x == 0):
            counterComputer += 1
            if(counterComputer > 3):
                print('NO')
                return
        else:
            counterComputer = 0
            flag = True
    if(flag):
        print('YES')
    else:
        print('NO')

yesOrNo()
    