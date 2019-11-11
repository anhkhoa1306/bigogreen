txt = input()
sum = 0
for n in txt:
    sum += int(n)
print('{0}'.format(str(sum).strip()[-1]))