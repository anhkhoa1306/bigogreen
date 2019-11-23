def rickAndMorty():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    rickStep = 0
    mortyStep = 0
    rick = b
    morty = d
    loop = 0
    while(True):
        loop += 1
        if(loop == 10000):
            print(-1)
            return
        if(rick == morty):
            print(rick)
            return
        if(rick > morty):
            morty = d + mortyStep * c
            mortyStep += 1
        elif(rick < morty):
            rick = b + rickStep * a
            rickStep += 1

rickAndMorty()