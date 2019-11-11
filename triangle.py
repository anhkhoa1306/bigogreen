import math
a, b, c = map(float, input().split())
cv = a + b + c
p = cv / 2
dt = math.sqrt(p * (p-a) * (p-b) * (p-c))
print('{0:.2f} {1:.2f}'.format(cv, dt))

