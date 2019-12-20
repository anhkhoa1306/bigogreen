class Employee:
    def __init__(self, c = "", n = "", y = 0):
        self.c = c
        self.n = n
        self.y = y

    def display(self):
        print("{0} {1} {2}".format(self.c, self.n, self.y))

class EmployeeCollection:
    def __init__(self, e = []):
        self.e = e
    
    def sort(self):
        for x in range(len(self.e)):
            i = x + 1
            while(i < len(self.e)):
                if(self.e[x].y > self.e[i].y):
                    temp = self.e[x]
                    self.e[x] = self.e[i]
                    self.e[i] = temp
                i += 1
        
        for z in range(len(self.e)):
            j = z + 1
            while(j < len(self.e)):
                if(self.e[z].y == self.e[j].y):
                    if(int(self.e[z].c) > int(self.e[j].c)):
                        temp = self.e[z]
                        self.e[z] = self.e[j]
                        self.e[j] = temp
                j += 1
    
    def display(self):
        self.e[0].display()

def solution():
    n = int(input())
    ee = []
    while(n > 0):
        c, m, y = map(str, input().split())
        e = Employee(c, m, int(y))
        ee.append(e)
        n -= 1
    ec = EmployeeCollection(ee)
    ec.sort()
    ec.display()

solution()