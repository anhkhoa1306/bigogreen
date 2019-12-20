import math
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        s = "{0} {1}".format(self.x, self.y)
        return s
        
    def distance(self, p2):
        xD = math.pow((self.x - p2.x), 2)
        yD = math.pow((self.y - p2.y), 2)
        d = math.sqrt(xD + yD)
        return d

class PointCollection():
    def __init__(self, p = []):
        self.p = p
    
    def sort(self, s):
        for x in range(len(self.p)):
            y = x + 1
            while(y < len(self.p)):
                xD = s.distance(self.p[x])
                yD = s.distance(self.p[y])
                if(yD > xD):
                    t = self.p[x]
                    self.p[x] = self.p[y]
                    self.p[y] = t
                y += 1

    def display(self):
        print(self.p[0])

def solution():
    x, y = map(int, input().split())
    n = int(input())
    s = Point(x, y)
    a = []
    while(n > 0):
        xx, yy = map(int, input().split())
        p = Point(xx, yy)
        a.append(p)
        n -= 1

    pp = PointCollection(a)
    pp.sort(s)
    pp.display()

solution()
