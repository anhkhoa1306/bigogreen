class Student:
    def __init__(self, c = "", m = "", l = ""):
        self.c = c
        self.m = m
        self.l = l
    def lookUp(self, c):
        if(self.c == c):
            print(self)
        return 
    def __str__(self):
        s = "{0} {1}".format(self.m, self.l)
        return s
def solution():
    n, k = map(int, input().split())
    a = []
    q = []
    while(n > 0):
        c, m, l = map(str, input().split())
        s = Student(c, m ,l)
        a.append(s)
        n -= 1

    while(k > 0):
        q.append(input())
        k -= 1

    for x in range(len(q)):
        for y in range(len(a)):
            a[y].lookUp(q[x])

solution()