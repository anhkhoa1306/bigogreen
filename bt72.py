class Coordinate:
    def __init__(self, x, y ,v):
        self.x = x
        self.y = y
        self.v = v
    def __str__(self):
        s = "{0} {1}".format(self.x, self.y)
        return s

class CoordinateCollection:
    def __init__(self, c = []):
        self.c = c
    def display(self):
        a = []
        for x in range(len(self.c)):
            if(self.c[x].v <= 0):
                continue
            a.append(self.c[x])
        print(len(a))
        for y in range(len(a)):
            print(a[y])

def solution():
    row, column = map(int, input().split())
    k = int(input())
    cc = []
    while(k > 0):
        x, y, v = map(int, input().split())
        c = Coordinate(x, y, v)
        cc.append(c)
        k -= 1
    
    collection = CoordinateCollection(cc)
    collection.display()

solution()
