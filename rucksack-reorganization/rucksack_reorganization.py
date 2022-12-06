#Day 3 solution

def convertInputToList(txtFile):
    #inputList = []
    with open(txtFile) as inputFile:
        inputList = inputFile.read().splitlines()
        #inputList = inputFile.readlines()
    return inputList

example_File = 'example_input.txt'
exampleInputList = convertInputToList(example_File)
#print(exampleInputList)

#item is character/letter
#lowercase code point range for a-z is 97-122
"""Lowercase item types a through z have priorities 1 through 26."""
#97 - 96 = 1
def convertLowerToPriority(item):
    return ord(item)-96

#uppercase code point range for A-Z is 65-90
"""Uppercase item types A through Z have priorities 27 through 52."""
#65 - 38 = 27
def convertUpperToPriority(item):
    return ord(item)-38

def findCommonItem(rucksack):
    firstCompartment = set()
    for index in range(0, int(len(rucksack)/2)):
        firstCompartment.add(rucksack[index])
    for index in range(int(len(rucksack)/2), len(rucksack)):
        if rucksack[index] in firstCompartment:
            return rucksack[index]

#commonItem = findCommonItem('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
#print(commonItem)

def calculatePrioritySum(rucksackList):
    prioritySum = 0
    for rucksack in rucksackList:
        commonItem = findCommonItem(rucksack)
        if commonItem.islower():
            prioritySum = prioritySum + convertLowerToPriority(commonItem)
        else:
            prioritySum = prioritySum + convertUpperToPriority(commonItem)
    return prioritySum

def findPartOneAnswer(txtFile):
    inputList = convertInputToList(txtFile)
    partOneAnswer = calculatePrioritySum(inputList)
    print(partOneAnswer)
    return partOneAnswer

#findPartOneAnswer('example_input.txt')

#findPartOneAnswer('input.txt')

#8053

def findCommonItemSolution2(rucksack):
    for index in range(0, int(len(rucksack)/2)):
        if rucksack[index] in rucksack[int(len(rucksack)/2):]:
            return rucksack[index]

def calculatePrioritySumSolution2(rucksackList):
    prioritySum = 0
    for rucksack in rucksackList:
        commonItem = findCommonItemSolution2(rucksack)
        if commonItem.islower():
            prioritySum = prioritySum + convertLowerToPriority(commonItem)
        else:
            prioritySum = prioritySum + convertUpperToPriority(commonItem)
    return prioritySum

def findPartOneAnswerSolution2(txtFile):
    inputList = convertInputToList(txtFile)
    partOneAnswer = calculatePrioritySumSolution2(inputList)
    print(partOneAnswer)
    return partOneAnswer

#findPartOneAnswerSolution2('input.txt')



