#FAILED TERRIBLY
totalPeople, peopleWithBoats, totalFriendPairs = map(int, input().split())
boatIndexes = set(list(map(int, input().split())))
peopleReferenced = set(x for x in range(1,totalPeople+1)).difference(boatIndexes)

dontNeedABoat = 0
for i in range(totalFriendPairs):
    friends = set(list(map(int, input().split())))

    peopleReferenced = peopleReferenced.difference(friends)

    if(len(boatIndexes) == len(boatIndexes.difference(friends)) or len(boatIndexes) == (len(boatIndexes.difference(friends))-1)):
        continue
    else:
        dontNeedABoat += 1

print(len(peopleReferenced))
boatsNeeded = ((totalPeople-peopleWithBoats)-dontNeedABoat)+(len(peopleReferenced))

###TESTING PURPOSES###
print(f"\n\nTotal People: {totalPeople}\nNumber of people with Boats: {peopleWithBoats}\nTotal Number of Friends: {totalFriendPairs}\nWho has boats: {list(boatIndexes)}\nWho doesn't need a boat: {dontNeedABoat}\n\n**************\nBOATS NEEDED ---> {boatsNeeded}")

###SOLUTION###
##print(boatsNeeded)