def solution():
    n = int(input())
    product = recursive(n)
    print(product)

def recursive(n):
    if(n == 0):
        return 1
    return n * recursive(n - 1)

solution()