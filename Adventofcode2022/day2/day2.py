f = open("inputday2.txt", "r")
rounds = f.readlines()

point = 0
for round in rounds:
    if round.split()[1] == 'X':         #rock
        point += 1
        if round.split()[0] == 'A':     #rock
            point += 3
        elif round.split()[0] == 'B':   #paper
            point +=0
        else:                           #scissor
            point += 6
    
    if round.split()[1] == 'Y':         #paper
        point += 2
        if round.split()[0] == 'A':     #rock
            point += 6
        elif round.split()[0] == 'B':   #paper
            point +=3
        else:    #scissor
            point += 0
    
    if round.split()[1] == 'Z':         #scissor
        point += 3
        if round.split()[0] == 'A':     #rock
            point += 0
        elif round.split()[0] == 'B':   #paper
            point +=6
        else:                           #scissor
            point += 3

print(point)