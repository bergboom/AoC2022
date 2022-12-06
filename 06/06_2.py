def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

combination =[]
isFound = False
x = 0
inSequence = 14
with open('input.txt') as f:
    line = f.readlines()[0].replace('\n','').strip()
    while x < len(line):
        letter = line[x]
        if(len(combination) < inSequence - 1):
            combination.append(letter)
        else:
            if letter in combination:
                del combination[0]
            else:
                if(len(combination) > inSequence-1):
                    del combination[0]
            combination.append(letter)
            if(len(combination) == inSequence):
                if(allUnique(combination)):
                    break
        x += 1
print(combination, x+1)