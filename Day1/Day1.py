inputList = []
fileName = ".\\adventofcode2018\\Day1\\input.txt"
def calibrateOutput (input, output):
    output = output + input
    return output;

def findRepeatedFrequency(providedList):
    processedList = []
    frequency = 0
    
    for change in providedList:
        processedList.append(frequency)
        frequency = calibrateOutput(change, frequency)
        if frequency in processedList:
            return frequency;

file = open(fileName, "r")
for line in file:    
    inputList.append(int(line))
file.close();

print(findRepeatedFrequency(inputList))