#Day 2 solution

def convertInputToList(txtFile):
    inputList = []
    with open(txtFile) as inputFile:
        for line in inputFile.readlines():
            inputList.append(line.strip().split())
    return inputList

#example_File = 'example_input.txt'
#exampleInputList = convertInputToList(example_File)
#print(exampleInputList)

"""The score for a single round is the score for the shape you selected
(
1 for Rock,
2 for Paper, and
3 for Scissors
)
plus the score for the outcome of the round
(
0 if you lost,
3 if the round was a draw, and
6 if you won)."""

"""The first column is what your opponent is going to play:
A for Rock,
B for Paper, and
C for Scissors."""

"""The second column, you reason, must be what you should play in response:
X for Rock,
Y for Paper, and
Z for Scissors."""

#roundList has 2 values [opponentChoice, playerChoice]
def calculateRoundScore(roundList):
    opponentKey = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
    playerKey = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
    # scoreKey from player's perspective
    # key is player's choice
    # value is opponent's choice
    shapeScoreKey = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3
    }
    outcomeScoreKey = {
        'Rock': {'Rock': 3, 'Paper': 0, 'Scissors': 6},
        'Paper': {'Rock': 6, 'Paper': 3, 'Scissors': 0},
        'Scissors': {'Rock': 0, 'Paper': 6, 'Scissors': 3}
    }
    roundScore = shapeScoreKey[playerKey[roundList[-1]]] + outcomeScoreKey[playerKey[roundList[-1]]][opponentKey[roundList[0]]]
    return roundScore

#testRoundList = ['A', 'Y']
#roundScore = calculateRoundScore(testRoundList)
#print(roundScore)

#game has multiple rounds
#game is a list of lists where each smaller list is a roundList
def calculateTotalScore(gameList):
    totalScore = 0
    for round in gameList:
        totalScore = totalScore + calculateRoundScore(round)
    return totalScore

def findPartOneAnswer(txtFile):
    inputList = convertInputToList(txtFile)
    partOneAnswer = calculateTotalScore(inputList)
    return partOneAnswer

partOneAnswer = findPartOneAnswer('input.txt')
print(partOneAnswer)

#15691
