def isInSameRange(firstGroup, secondGroup):
    firstPair = firstGroup.split('-')
    secondPair = secondGroup.split('-')
    if((int(firstPair[0]) <= int(secondPair[0]) and int(firstPair[1]) >= int(secondPair[1])) 
    or (int(secondPair[0]) <= int(firstPair[0]) and int(secondPair[1]) >= int(firstPair[1]))):
        return True;
    else:
        return False;

def isOverlapping(firstGroup, secondGroup):
    firstPair = firstGroup.split('-')
    secondPair = secondGroup.split('-')
    isOverlap = False
    if(int(secondPair[1])-int(secondPair[0]) > int(firstPair[1])-int(firstPair[0])):
        for x in range(int(secondPair[0]), int(secondPair[1])+1):
            if((int(firstPair[0]) == x) or (int(firstPair[1]) == x)):
                isOverlap = True
                break
    else:
        for x in range(int(firstPair[0]), int(firstPair[1])+1):
            if((int(secondPair[0]) == x) or (int(secondPair[1]) == x)):
                isOverlap = True
                break
    return isOverlap

numberOfOverlaps = 0
numberOfOverlaps_Part2 = 0

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
         currentLine = line.replace("\n", "" ).strip()
         currentLine = currentLine.split(',')
         if(isInSameRange(currentLine[0],currentLine[1])):
            numberOfOverlaps += 1
         if(isOverlapping(currentLine[0],currentLine[1])):
            numberOfOverlaps_Part2 += 1

print("Part 1: Number of Overlaps:", numberOfOverlaps)
print("Part 2: Number of Overlaps:", numberOfOverlaps_Part2)
