def isFullyContained(elf1, elf2):
    return (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1])

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


def main():
    amountOfFullyContainedElfpairs = 0
    inputlist = importinput(path)
    for elfpair in inputlist:
        elfpair = stringTolist(elfpair)
        if isFullyContained(elfpair[0], elfpair[1]) == True:
            amountOfFullyContainedElfpairs += 1
    return print(amountOfFullyContainedElfpairs)

path = "C:/Users/Theo/Documents/Adventofcode2022/advent-of-code-2022/Adventofcode2022/day4/inputday4.txt"
main()

groda groda


