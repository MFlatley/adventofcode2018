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

def compareStrings(first,second):
    i=0
    compiledString = []
    while i< len(first)-1:
        if first[i] == second[i]:
            compiledString.append(first[i])
        i += 1
    if len(compiledString) == len(first)-2:
        return compiledString
    else:
        return "Not prototype"

def findPrototype (inList):
    j=0
    k=0
    outputMessage = "Not prototype"
    while j< len(inList):
        if k < len(inList):
            outputMessage = compareStrings(inList[j],inList[k])
            k += 1
            if outputMessage != "Not prototype":
                return outputMessage
        else:
            k = 0
            j += 1
    
file = open(fileName, "r")
for line in file:    
    inputList.append(line)
file.close();

for line in inputList:
    doubleTracker += findDoubles(line)
    tripleTracker += findTriples(line)

print(doubleTracker*tripleTracker)
print(findPrototype(inputList))