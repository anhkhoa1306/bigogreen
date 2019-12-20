import math
class Triangle:
    def __init__(self, a = 1, b = 1, c = 1):
        self.a = a
        self.b = b
        self.c = c
    def dt(self):
        s = (self.a + self.b + self.c) / 2
        dt = math.sqrt(s*((s - self.a)*(s - self.b)*(s - self.c)))
        return dt

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

def solution():
    n = int(input())
    d = 0
    while(n > 0):
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        x3, y3 = map(int, input().split())
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        a = p1.distance(p2)
        b = p1.distance(p3)
        c = p2.distance(p3)
        t = Triangle(a, b, c)
        d += t.dt()
        n -= 1
    print("{0:.2f}".format(d))
        
solution()