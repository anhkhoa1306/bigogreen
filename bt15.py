n = int(input())
m = n
a = ''
for i in range(1, n + 1):
    if(i != 1):
        a += '\n'
    for j in range(1, n + 1):
        if(i == 1 or i == n):
            a += '*'
        elif(j == 1 or j == n):
            a += '*'
        else:
            a += ' '
print(a)