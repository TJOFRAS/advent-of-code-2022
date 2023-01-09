f = open("C:/Users/Theo/Documents/Adventofcode2022/advent-of-code-2022/Adventofcode2022/day3/inputday3.txt", "r")
packs = f.readlines()
groups = []
while packs != []:
    groups.append(packs[:3])
    packs = packs[3:]
print(groups[0])

sum = 0
for comp in groups:
    for i in comp[0]:
        if i in comp[1] and i != "\n":
            if i in comp[2]:
                a = ord(i)
                if i.isupper() == True:
                    a -= 38
                else:
                    a -= 96
    sum += a    
print(sum)
