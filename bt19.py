def totalDigit():
    i = int(input())
    total = 1
    while(i >= 10):
        total += 1
        i = i / 10
    print(total)

totalDigit()