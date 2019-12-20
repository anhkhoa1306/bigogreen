def resursive(ar, index):
    if(index == len(ar) - 1):
        return ar[index]
    return ar[index] + resursive(ar, index + 1)

def simpleArraySum(ar):
    total = resursive(ar, 0)
    print(total)

simpleArraySum([1,2,3,4,10,11])