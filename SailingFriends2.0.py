from collections import defaultdict

totalPeople, totalBoatPeople, totalFriendPairs = map(int, input().split())
allPeopleList = set([x for x in range(1,totalPeople+1)])
boatList = set(list(map(int, input().split())))
friendList = defaultdict(set)

for i in range(totalFriendPairs):
    friend1, friend2 = map(int, input().split())
    friendList[friend1].add(friend2)
    friendList[friend2].add(friend1)

peopleToAdd = set()
for person in boatList:
    if person in friendList:
        for person2 in friendList.get(person):
            peopleToAdd.add(person2)
        
boatList = boatList | peopleToAdd
peopleWhoNeedBoats = allPeopleList.difference(boatList)

boatsNeeded = 0
peopleToSubtract = set()
for person in peopleWhoNeedBoats:
    if person in friendList and person not in peopleToSubtract:
        boatsNeeded+=1
        peopleToSubtract.add(person)
        for person2 in friendList.get(person):
            peopleToSubtract.add(person2)

    elif person not in friendList and person not in peopleToSubtract:
        boatsNeeded+=1
        peopleToSubtract.add(person)
    else:
        peopleToSubtract.add(person)

print(boatsNeeded)