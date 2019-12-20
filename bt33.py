def total(array):
    total = 0
    for x in array:
        total += x
    return total

def solution():
    m, n = map(int, input().split())
    text = ""
    for i in range(m):
        temp = list(map(int, input().split()))
        text += str(i) + ": " + str(total(temp))
        if(i != (m-1)):
            text += "\n"
    print(text)
solution()