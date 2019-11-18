min = 10
max = 0
while(1 == 1):
    s = int(input())
    if(s > max):
        max = s
    if(s >= 0 and s < min):
        min = s
    if(s == -1):
        break
print('{0} {1}'.format(int(max), int(min)))