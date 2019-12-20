def recursive(n, star, space):
    if(star == n):
        printStarRecursive(star)
        return
    else:
        printSpaceRecursive(space)
        printStarRecursive(star)
    recursive(n, star + 1, space - 1)
    
def printStarRecursive(n):
    if(n == 1):
        print("#")
        return
    print("#", end = "")
    printStarRecursive(n - 1)

def printSpaceRecursive(n):
    if(n == 0):
        return
    print(" ", end = "")
    printSpaceRecursive(n - 1)

def staircase(n):
    recursive(n, 1, n - 1)

staircase(6)