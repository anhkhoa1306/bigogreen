def largestDigit():
    n = str(input())
    max = 0
    for c in n:
        cv = int(c)
        if(cv > max):
            max = cv
    print(max)

largestDigit()