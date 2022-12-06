#Day 1 solution

from queue import PriorityQueue

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

def findPartOneAnswer(txtFile):
    inputList = convertInputToList(txtFile)
    partOneAnswer = findMaxSum(inputList)
    print(partOneAnswer)
    return partOneAnswer

#findPartOneAnswer('input.txt')

#71502


def findTopThreeSum(elfList):
    topThreeQ = PriorityQueue()
    for elf in elfList:
        caloriesSum = sumElfCalories(elf)
        #print(caloriesSum)
        topThreeQ.put(caloriesSum)
        if topThreeQ.qsize() > 3:
            topThreeQ.get()
    topThreeSum = 0
    while not topThreeQ.empty():
        topThreeSum += topThreeQ.get()
    return topThreeSum

def findPartTwoAnswer(txtFile):
    inputList = convertInputToList(txtFile)
    partTwoAnswer = findTopThreeSum(inputList)
    print(partTwoAnswer)
    return partTwoAnswer

#findPartTwoAnswer('input.txt')

#208191

