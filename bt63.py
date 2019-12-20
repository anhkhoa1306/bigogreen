def solution():
    n = int(input())
    t = recursive(n)
    print(t)

def recursive(n):
    if(n == 0 or n == 1):
        return 1
    return recursive(n - 1) + recursive(n - 2)
solution()