def solution():
    m = input()
    a = []

    previous = ""
    for x in range(len(m)):
        if(previous == "" or previous == " "):
            a.append(m[x].upper())
        previous = m[x]
    
    l = len(a)
    for y in range(l):
        if(y == l - 1):
            print(a[y])
        else:
            print(a[y], end = "")

solution()
