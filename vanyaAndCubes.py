i = int(input())
total = 0
cubes = 0
row = 1
totalCubes = 0
while(i >= 0):
    cubes += row
    row += 1
    i -= cubes
    if(i >= 0):
        total += 1

print(total)