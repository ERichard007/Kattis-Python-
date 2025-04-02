numContestants = int(input())
nameAndGuess = {}
for x in range(numContestants):
    name, guess = input().split()
    nameAndGuess[int(guess)] = name
sortedNums = sorted(nameAndGuess.keys())

for x in range(int(input())):
    idea = int(input())

    highIndex = len(sortedNums)-1
    lowIndex = 0
    midIndex = int((len(sortedNums)-1)/2)

    winnerName = None

    if idea >= sortedNums[highIndex]:
        winnerName = nameAndGuess.get(sortedNums[highIndex])
    else:
        while (lowIndex <= highIndex):
            midNum = sortedNums[midIndex]
            lowNum = sortedNums[lowIndex]
            highNum = sortedNums[highIndex]

            if (idea == midNum):
                winnerName = nameAndGuess.get(midNum)
                break
            elif (idea > midNum):
                winnerName = nameAndGuess.get(midNum)
                lowIndex = midIndex+1
                midIndex = int((lowIndex + highIndex)/2)
            else:
                highIndex = midIndex-1
                midIndex = int((lowIndex + highIndex)/2)

    if winnerName: 
        print(winnerName) 
    else: 
        print(":(")




    

