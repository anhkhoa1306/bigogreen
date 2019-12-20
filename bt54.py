def solution():
    m = int(input())
    i = 1
    while(i <= m):
        star = (i * 2) - 1
        leftSpace = m - i 
        while(leftSpace > 0):
            print(" ", end = "")
            leftSpace -= 1

        for x in range(star):
            print("*", end = "")

        rightSpace = m - 1 
        while(rightSpace > 0):
            print(" ", end = "")
            rightSpace -= 1

        print()
        i += 1

solution()