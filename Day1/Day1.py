finalOutput = 0
thisList = []
fileName = ".\\adventofcode2018\\Day1\\input.txt"
def calibrateOutput (input, output):
    output = output + input
    return output;

while  True:
    file = open(fileName,"r")
    for line in file:
        if finalOutput in thisList:
            print(finalOutput)
            False;
        else:
            thisList.append(finalOutput)
        finalOutput = calibrateOutput(int(line),finalOutput)
    file.close();