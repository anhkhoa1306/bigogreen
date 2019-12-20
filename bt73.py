class Fraction:
    def __init__(self, num = 0, denom = 1):
        self.num = num
        self.denom = denom
    
    def floatValue(self):
        s = self.num / self.denom
        return s

    def gcd(self, a, b):
        r = 0
        while(b != 0):
            r = a % b
            a = b
            b = r
        return a
        
    def display(self, n):
        s = "{0} {1}".format(int(self.num / n), int(self.denom / n))
        print(s)

class FractionCollection:
    def __init__(self, f = []):
        self.f = f
    
    def sort(self):
        for x in range(len(self.f)):
            y = x + 1
            while(y < len(self.f)):
                if(self.f[y].floatValue() > self.f[x].floatValue()):
                    temp = self.f[x]
                    self.f[x] = self.f[y]
                    self.f[y] = temp
                y += 1
    
    def display(self):
        a = self.f[0].gcd(self.f[0].num, self.f[0].denom)
        self.f[0].display(a)

def solution():
    n = int(input())
    fc = []
    while(n > 0):
        a, b = map(int, input().split())
        f = Fraction(a, b)
        fc.append(f)
        n -= 1
    collection = FractionCollection(fc)
    collection.sort()
    collection.display()

solution()
