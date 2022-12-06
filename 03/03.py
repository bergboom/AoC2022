import numpy as np

def getCharacterValue(values):
    totalValue = 0
    for letter in values:
        if(letter.islower()):
            totalValue += ord(letter)-96 #Get Value based on a = 1 from ascii
        else:
            totalValue += ord(letter)-64+26 #Get Value based on A = 27 from ascii
    return totalValue

def findUniqueBadge(arrIn):
    foundBadge = np.intersect1d(arrIn[0],arrIn[1])
    foundBadge = np.intersect1d(foundBadge,arrIn[2])
    #print("Badge:",foundBadge)
    return getCharacterValue(foundBadge)


arrItems = np.array([])
arrList = []
counter = 0
unique = []
with open('input/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        currentLine = line.replace("\n", "" ).strip()
        #Part 1 - START
        arrFirstCompartment = list(currentLine[0:int(len(currentLine)/2)])
        arrSecondCompartment = list(currentLine[int(len(currentLine)/2):])
        repeatedItems = np.intersect1d(arrFirstCompartment,arrSecondCompartment)
        arrItems = np.append(arrItems, getCharacterValue(repeatedItems) , axis=None)
        #Part 1 - END

        #Part 2 - START
        if(counter < 2):
            counter += 1
            arrList.append(list(currentLine))
            
        else:
            arrList.append(list(currentLine))
            unique.append(findUniqueBadge(arrList))
            counter = 0
            arrList = []
        #Part 2 - END

print("Result Part 1:", np.sum(arrItems))
arrBadges = np.array(unique)
print("Result Part 2:", np.sum(arrBadges))