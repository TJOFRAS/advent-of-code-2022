def isFullyContained(elf1, elf2):
    return elf1[0] < elf2[0] and elf1[1] > elf2[1]
    
def convertElfsToInt
f = open("C:/Users/Theo/Documents/Adventofcode2022/advent-of-code-2022/Adventofcode2022/day4/inputday4.txt", "r")
fileContent = f.readlines()

for workingPairs in fileContent:

    workingPairs = workingPairs.replace("\n","")
    workingPairs = workingPairs.split(",")
    workingPairs = [workingPairs[0].split("-") , workingPairs[1].split("-")]
    print(workingPairs)