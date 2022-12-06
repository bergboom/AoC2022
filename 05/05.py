columns = []


def getCratesIntoStorage(line):
    columnNumber = 0
    for index in range (1, len(line),4):
        if(line[index] != ' '):
            columns.append([columnNumber,line[index:index+1]])
        columnNumber += 1

def createColumns(noOfColumns):
    cols = []
    i = 0
    x = len(columns)-1
    while i < noOfColumns:
        cols.append([])
        i += 1
    while x >= 0:
        c = columns[x]
        if(c[1] != ' '):
            cols[int(c[0])].append(c[1])
        x -= 1
    return cols

def movement(storage,input):
    str1 =input.split(' ')
    #print(input)
    #print(storage)
    i = 0
    while i < int(str1[1]):
        if(len(storage[int(str1[3])-1]) > 0):
            value = storage[int(str1[3])-1].pop()
            storage[int(str1[5])-1].append(value)
        i += 1
    return storage

noOfColumns = 0
readColumns = True
storageRow = []
r = []

with open("input05.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n","")
        if(len(line)> 1):
            c1 = str(line[1])
            if(not readColumns):
                storageRow = movement(storageRow,line) #Follow movement
            if( not c1.isnumeric() and readColumns):
                getCratesIntoStorage(line)
            if( c1.isnumeric() and readColumns):
                noOfColumns = int(line[len(line)-2:len(line)-1])
                readColumns = False
                storageRow = createColumns(noOfColumns)
for c in storageRow:
    print(c[-1],end="")