f = open("C:/Users/Theo/Documents/Adventofcode2022/advent-of-code-2022/Adventofcode2022/day3/inputday3.txt", "r")
packs = f.readlines()
sum = 0
for comp in packs:
    length = len(comp)
    splitted = comp[0:length//2]
    splitted2 = comp[length//2:]
    res = str("")
    for i in splitted:
        if i in splitted2 :
            a = ord(i)
            if i.isupper() == True:
                a -= 38
            else:
                a -= 96
    sum += a    
print(sum)
