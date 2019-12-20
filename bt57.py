def solution():
    n = int(input())
    r = recursive(n, n)
    print(int(r))

def recursive(n, m):
    if(n % m == 0 and m % 2 != 0):
        return m
    return recursive(n, m / 2)

solution()