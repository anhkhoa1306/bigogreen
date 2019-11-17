a, b, c , d = map(int, input().split())
max = a
if(b > max):
    max = b
if(c > max):
    max = c
if(d > max):
    max = d
print(max)