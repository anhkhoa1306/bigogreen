class Paper:
    def __init__(self, c = 0, l = 0):
        self.c = c
        self.l = l
    
class PaperCollection:
    def __init__(self, p):
        self.p = p
    
    def sort(self):
        for x in range(len(self.p)):
            y = x + 1
            while(y < len(self.p)):
                if(self.p[x].c > self.p[y].c):
                    temp = self.p[x]
                    self.p[x] = self.p[y]
                    self.p[y] = temp
                y += 1

    def display(self):
        previousCode = 0
        totalColor = 0
        a = []
        for y in range(len(self.p)):
            totalColor += 1
            total = 1
            l = self.p[y].l
            if(self.p[y].c == previousCode):
                totalColor -= 1
                continue
            for z in range(len(self.p)):
                if(y != z and self.p[y].c == self.p[z].c):
                   previousCode = self.p[y].c 
                   total += 1
                   l += self.p[z].l
            a.append("{0} {1} {2}".format(self.p[y].c, l, total)) 
            
        print(totalColor)
        for x in range(len(a)):
            print(a[x])

def solution():
    n = int(input())
    pp = []
    while(n > 0):
        c, l = map(int, input().split())
        p = Paper(c, l)
        pp.append(p)
        n -= 1
    pc = PaperCollection(pp)
    pc.sort()
    pc.display()

solution()
            
    
    