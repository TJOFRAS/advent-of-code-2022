def isFullyContained(elfpair, elf2):
    return (elfpair[0] <= elf2[0] and elfpair[1] >= elf2[1]) or (elfpair[0] >= elf2[0] and elfpair[1] <= elf2[1])

def importinput(path):
    input = open(path, "r")
    inputlist = input.readlines()
    return inputlist

def stringTolist(string):
    stringsplitted = string.split(',')
    string1 = stringsplitted[0]
    string2 = stringsplitted[1]
    string1 = string1.split('-')
    string2 = string2.split('-')
    cleanList = [int(string1[0]), int(string1[1])],[ int(string2[0]), int(string2[1])]
    return cleanList

def makeListOfAllAreas(elfpair):
    areaself1 = []
    areaself2 = []
    for number in range(elfpair[0][0], elfpair[0][1]+1):
        areaself1.append(number)
    for number in range(elfpair[1][0], elfpair[1][1]+1):
        areaself2.append(number)
    elfpair = areaself1, areaself2
    return elfpair

def areTheyOverlaping(elfpair):
    for number in elfpair[0]:
        if number in elfpair[1]:
            return True

def main():
    inputlist = importinput(path)

    amountOfFullyContainedElfpairs = 0
    for elfpair in inputlist:
        elfpair = stringTolist(elfpair)
        if isFullyContained(elfpair[0], elfpair[1]) == True:
            amountOfFullyContainedElfpairs += 1

    return print(amountOfFullyContainedElfpairs)

def main2():
    inputlist = importinput(path)

    amountOfFullyContainedElfpairs = 0
    for elfpair in inputlist:
        elfpair = stringTolist(elfpair)
        elfpair = makeListOfAllAreas(elfpair)
        if areTheyOverlaping(elfpair) == True:
            amountOfFullyContainedElfpairs += 1

    return print(amountOfFullyContainedElfpairs)

path = "C:/Users/Theo/Documents/Adventofcode2022/advent-of-code-2022/Adventofcode2022/day4/inputday4.txt"
main()
main2()