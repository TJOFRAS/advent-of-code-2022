#create a program wich prints groda
print('groda')
#read in values from inputday1.txt
f = open("inputday1.txt", "r")
##print(f.read())

#create list of sum of each elfs calories
fooditems = f.readlines()
##print(fooditems[0])
caloriesum = 0

#print(fattestelfsorted)
#print(fattestelfsorted[2])
fattestelfsorted =  [0] * 3
#print(fattestelfsorted[2])
for calorie in fooditems:
    if calorie == "\n":
        if caloriesum > fattestelfsorted[0]:
            fattestelfsorted[0] = caloriesum
            fattestelfsorted.sort()
        caloriesum = 0

    else:
        caloriesum += int(calorie)

print(sum(fattestelfsorted))



#search said list of the largest value