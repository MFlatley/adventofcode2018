finalOutput = 0
thisList = []
inputList = []
fileName = ".\\adventofcode2018\\Day1\\input.txt"
def calibrateOutput (input, output):
    output = output + input
    return output;

file = open(fileName, "r")
for line in file:
    inputList.append(int(line))
file.close();

while  finalOutput not in thisList:    
    for change in inputList:
        thisList.append(finalOutput)
        finalOutput = calibrateOutput(change,finalOutput)
print(finalOutput)