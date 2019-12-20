def solution():
    n = int(input())
    if(n < 0):
        n = n * (-1)
    a = n % 10
    r = recursive(n, a)
    print(r)

def recursive(n, a):   
    b = n % 10
    if(n / 10 < 1):
        if(b > a):
            return b
        return a
    if(a > b):
        return recursive(int(n/10), a)
    else:
        return recursive(int(n/10), b)

solution()
    
