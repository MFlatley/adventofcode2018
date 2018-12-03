inputList = []
fileName = ".\\adventofcode2018\\Day1\\input.txt"
def calibrateOutput (input, output):
    output = output + input
    return output;

def findRepeatedFrequency(providedList):
    processedList = {0}
    frequency = 0
    while True:
        for change in providedList:
            
            frequency = calibrateOutput(change, frequency)
            if frequency in processedList:
                return frequency;
            else:
                processedList.add(frequency)

file = open(fileName, "r")
for line in file:    
    inputList.append(int(line))
file.close();

print(findRepeatedFrequency(inputList))