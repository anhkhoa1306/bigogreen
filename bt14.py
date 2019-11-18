def func():
    n = int(input())
    while(n>0):
        x = int(input())
        if(x % 2 != 0):
            print('NO')
            return
        n -= 1
    print('YES')

func()