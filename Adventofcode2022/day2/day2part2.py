f = open("C:/Users/Theo/Documents/Adventofcode2022/advent-of-code-2022/Adventofcode2022/day2/inputday2.txt", "r")
rounds = f.readlines()

point = 0
for round in rounds:

# X = loose
# Y = draw
# Z = win

    if round.split()[1] == 'X':         #loose
        point += 0
        if round.split()[0] == 'A':     #rock
            point += 3
        elif round.split()[0] == 'B':   #paper
            point +=1
        else:                           #scissor
            point += 2
    
    if round.split()[1] == 'Y':         #draw
        point += 3
        if round.split()[0] == 'A':     #rock
            point += 1
        elif round.split()[0] == 'B':   #paper
            point +=2
        else:                           #scissor
            point += 3
            
    if round.split()[1] == 'Z':         #win
        point += 6
        if round.split()[0] == 'A':     #rock
            point += 2
        elif round.split()[0] == 'B':   #paper
            point +=3
        else:                           #scissor
            point += 1

print(point)