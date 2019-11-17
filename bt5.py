a, b = map(int, input().split())
lucky = int(input())
if(lucky % a == 0 and lucky % b == 0):
    print('Both')
elif(lucky % a == 0 and lucky % b != 0):
    print('Upan')
elif(lucky % a != 0 and lucky % b == 0):
    print('Ipan')
else:
    print('No')
