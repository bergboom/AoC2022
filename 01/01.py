import numpy as np

arr = np.array([])
heaviest = 0.0
current = 0.0
with open('Input/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        currentLine = line.replace("\n", "" ).strip()
        if currentLine == "":
            arr = np.append(arr, current, axis=None)
            if(current >= heaviest):
                heaviest = current
            current = 0.0
                
        else:
            current += float(currentLine)
arr = np.sort(arr)[::-1]
print("1: Heaviest: ", heaviest)
print("2: Sum of top 3 Heaviest:",arr[0]+arr[1]+arr[2])