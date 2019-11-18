def func():
    i = int(input())
    if(i <= 1):
        print('NO')
        return
    y = 2

    while(y < i - 1):
        if(i % y == 0):
            print('NO')
            return
        y += 1

    print('YES')

func()