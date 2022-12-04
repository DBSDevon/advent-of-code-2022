#Day 1 solution
def convertInputToList(txtFile):
    inputList = []
    with open(txtFile) as inputFile:
        newList = []
        for line in inputFile.readlines():
            if line == '\n':
                inputList.append(newList.copy())
                newList.clear()
            else:
                newList.append(int(line.strip()))
        inputList.append(newList.copy())
    return inputList

#example_File = 'example_input.txt'
#exampleInputList = convertInputToList(example_File)
#print(exampleInputList)

#puzzleInputFile = 'input.txt'
#puzzleInputList = convertInputToList(puzzleInputFile)
#print(puzzleInputList)

def sumElfCalories(caloriesList):
    caloriesSum = 0
    for calories in caloriesList:
        caloriesSum = caloriesSum + calories
    return caloriesSum

def findMaxSum(elfList):
    maxSum = 0
    for elf in elfList:
        caloriesSum = sumElfCalories(elf)
        if caloriesSum > maxSum:
            maxSum = caloriesSum
    return maxSum

def findAnswer(txtFile):
    inputList = convertInputToList(txtFile)
    answer = findMaxSum(inputList)
    return answer

#answer = findAnswer('example_input.txt')
#print(answer)

answer = findAnswer('input.txt')
print(answer)

#71502

