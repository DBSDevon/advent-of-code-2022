#Day 4 solution

def convertInputToList(txtFile):
    inputList = []
    with open(txtFile) as inputFile:
        for line in inputFile.readlines():
            assignmentPair = line.strip().split(',')
            assignmentPair = [sections.split('-') for sections in assignmentPair]
            assignmentPair = [[int(section) for section in sections] for sections in assignmentPair]
            inputList.append(assignmentPair)
    return inputList

#example_File = 'example_input.txt'
#exampleInputList = convertInputToList(example_File)
#print(exampleInputList)

"""for assignmentPair in exampleInputList:
    #print(assignmentPair)
    for sections in assignmentPair:
        #print(sections)
        for section in sections:
            print(section)
            print(type(section))"""

#for assignmentPair in exampleInputList:
#    print(assignmentPair)

def isFullyContained(assignmentPair):
    if (assignmentPair[0][0] >= assignmentPair[1][0]) and (assignmentPair[0][1] <= assignmentPair[1][1]):
        #return True
        return 1
    if (assignmentPair[1][0] >= assignmentPair[0][0]) and (assignmentPair[1][1] <= assignmentPair[0][1]):
        #return True
        return 1
    else:
        #return False
        return 0

def findTotalFullyContainedPairs(sectionAssignmentsList):
    totalFullyContainedPairs = 0
    for assignmentPair in sectionAssignmentsList:
        totalFullyContainedPairs = totalFullyContainedPairs + isFullyContained(assignmentPair)
    return totalFullyContainedPairs

def findPartOneAnswer(txtFile):
    inputList = convertInputToList(txtFile)
    partOneAnswer = findTotalFullyContainedPairs(inputList)
    return partOneAnswer

#partOneAnswer = findPartOneAnswer('input.txt')
#print(partOneAnswer)

#651