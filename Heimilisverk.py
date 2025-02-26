numChores = int(input())

choreList = []
seen = set()
seenAdd = seen.add

for x in range(numChores):
    newChore = str(input())
    if not (newChore in seen or seenAdd(newChore)): print(newChore)
