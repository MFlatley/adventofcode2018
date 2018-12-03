doubleTracker = 0
tripleTracker = 0
inputList = []
fileName = ".\\adventofcode2018\\Day2\\input.txt"
def findDoubles (input):
    doubleFound = False
    for letter in input:
        if input.count(letter) == 2:
            doubleFound = True
    if doubleFound:
        return 1
    else: 
        return 0

def findTriples (input):
    tripleFound = False
    for letter in input:        
        if input.count(letter) == 3:
            tripleFound = True;
    if tripleFound:
        return 1
    else: 
        return 0

file = open(fileName, "r")
for line in file:    
    inputList.append(line)
file.close();

for line in inputList:
    doubleTracker += findDoubles(line)
    tripleTracker += findTriples(line)

print(doubleTracker*tripleTracker)
