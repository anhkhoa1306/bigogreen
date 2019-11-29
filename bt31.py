def appleAndOrange():
    n = int(input())
    index = 1
    largestApple = 0
    largestOrange = 0
    looping = 0
    while(n > 0):
        looping += 1
        a = list(map(int, input().split()))
        if(a[0] > largestApple):
            index = looping
            largestApple = a[0]
            largestOrange = a[1]
        elif(a[0] == largestApple):
            if(a[1] > largestOrange):
                index = looping
                largestOrange = a[1]
        n -= 1
        
    print(index)

appleAndOrange()