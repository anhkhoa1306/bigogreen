import math
class Fraction:
    def __init__(self, a = 0, b = 1):
        self.num = a
        self.denom = b

    def gcd(self, a, b):
        r = 0
        while(b != 0):
            r = a % b
            a = b
            b = r
        return a

    def sumFraction(self, p2):
        p3 = Fraction()
        p3.num = self.num * p2.denom + self.denom * p2.num
        p3.denom = self.denom * p2.denom
        p3.reduceFraction()
        return p3

    def reduceFraction(self):
        if(self.num == 0):
            self.denom = 0
            return
        x = self.gcd(abs(self.num), abs(self.denom))
        self.num = self.num // x
        self.denom = self.denom // x
    def __str__(self):
        s = "{0} {1}".format(self.num, self.denom)
        return s

    

def solution():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    p1 = Fraction(a, b)
    p2 = Fraction(c, d)
    p3 = p1.sumFraction(p2)
    print(p3)

solution()