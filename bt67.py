class Student:
    def __init__(self, n = "", m = 0, l = 0):
        self.name = n
        self.math = m
        self.literature = l
    def average(self):
        av = (self.math + self.literature) / 2
        return av >= 9.0

def solution():
    n = int(input())
    total = 0
    while(n > 0):
        name = input()
        m, l = map(float, input().split())
        s = Student(name, m, l)
        if(s.average()):
            total += 1
        n -= 1
    print(total)

solution()