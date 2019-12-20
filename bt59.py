def solution():
    n = input()
    r = recursive(n, 0)
    print(r)

def recursive(n, index):
    a = ord(n[index])
    if(a >= ord('0') and a <= ord('9')):
        return n[index]
    return recursive(n, index + 1)

solution()