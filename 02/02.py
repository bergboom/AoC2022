import numpy as np

def translate(value):
    switcher = {
        'X': 1, #Rock
        'Y': 2, #Paper
        'Z': 3, #Scissor
        'A': 1, #Rock
        'B': 2, #Paper
        'C': 3, #Scissor
    }
    return switcher.get(value, "nothing")


def getPoints(playerA, playerB):
    if playerA > playerB:
        if(playerA == 3 and playerB == 1): #edge-case: Scissor beaten by rock
            return playerB + 6
        return playerB
    if playerA == playerB:
        return playerB+3
    if playerA < playerB:
        if(playerA == 1 and playerB == 3): #edge-case: Rock beats scissor
            return playerB
        return playerB+6

def getSignToUse(playerA, endResult):
    playerB = playerA
    if endResult == 1: #Lose
        if(playerA == 1): #edge-case: Scissor beaten by rock
            playerB = 3
        else:
            playerB -=1
        return playerB
    if endResult == 2: #Even
        return playerB + 3
    if endResult == 3: #Win
        if(playerA ==3): #edge-case: Rock beats scissor
            playerB = 1
        else:
            playerB+=1
        return playerB + 6
    

arr = np.array([])
arr2 = np.array([])
with open('INput/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        currentLine = line.replace("\n", "" ).strip()
        #Part 1: Get Points 
        result = getPoints(translate(currentLine.split(' ')[0]), translate(currentLine.split(' ')[1]))
        arr = np.append(arr, result , axis=None)
        #Part 2: Get Sign
        result2 = getSignToUse(translate(currentLine.split(' ')[0]), translate(currentLine.split(' ')[1]))
        arr2 = np.append(arr2, result2 , axis=None)

print("Result Part 1:", np.sum(arr))
print("Result Part 2:", np.sum(arr2))