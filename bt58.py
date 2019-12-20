def solution():
    n = int(input())
    if(n < 0):
        n = n * (-1)
    total = recursive(n)
    print(total)

def recursive(n):
    if(n / 10 < 1):
        return 1
    return 1 + recursive(n / 10)

solution()