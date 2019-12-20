class Apple:
    def __init__(self, w, p):
        self.w = w
        self.p = p

class AppleCollection:
    def __init__(self, a = []):
        self.a = a
        self.sa = a
    
    def sort(self):
        temp = []
        for ap in range(len(self.a)):
            temp.append(self.a[ap])
            
        for x in range(len(temp)):
            i = x + 1
            while(i < len(temp)):
                if(temp[x].w < temp[i].w):
                    t = temp[x]
                    temp[x] = temp[i]
                    temp[i] = t
                i += 1
        
        for z in range(len(temp)):
            j = z + 1
            while(j < len(temp)):
                if(temp[z].w == temp[j].w):
                    if(temp[z].p < temp[j].p):
                        t = temp[z]
                        temp[z] = temp[j]
                        temp[j] = t
                j += 1
        self.sa = temp
    
    def display(self):
        for apple in range(len(self.a)):
            if(self.a[apple].w == self.sa[0].w and self.a[apple].p == self.sa[0].p):
                print(apple)
                return

def solution():
    n = int(input())
    ac = []
    while(n > 0):
        w, p = map(int, input().split())
        a = Apple(w, p)
        ac.append(a)
        n -= 1
    
    apples = AppleCollection(ac)
    apples.sort()
    apples.display()

solution()
