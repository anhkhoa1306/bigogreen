#An elephant decided to visit his friend. 
# It turned out that the elephant's house is
# located at point 0 and his friend's house 
# is located at point x(x > 0) of the coordinate line.
#  In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. 
# Determine, what is the minimum number of steps he need to make in order 
# to get to his friend's house.
def elephant():
    i = int(input())
    s = 0
    if(i % 5 == 0):
        s = int(i / 5)
        print(int(s))
        return
    s = int(i/5)
    i = i % 5
    if(i % 4 == 0):
        s += int(i / 4)
        print(int(s))
        return
    s += int(i / 4)
    i = i % 4
    if(i % 3 == 0):
        s += int(i / 3)
        print(int(s))
        return
    s += int(i / 3)
    i = i % 3
    if(i % 2 == 0):
        s += int(i / 2)
        print(int(s))
        return
    s += int(i / 2)
    i = i % 2
    if(i % 1 == 0):
        s += int(i / 1)
        print(int(s))
        return
elephant()