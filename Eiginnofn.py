numOfResidents = int(input())

residentNames = {}
for i in range(numOfResidents):
    newName = input()
    name1, name2 = None, None
    if " " in newName:
        name1, name2 = newName.split()
        residentNames[name1] = name2
    else:
        residentNames[newName] = None

doorbellQueries = int(input())
for q in range(doorbellQueries):
    findName = input()

    if findName in residentNames:
        if residentNames[findName] != None:
            print(f"Neibb en {findName} {residentNames[findName]} er heima")
        else:
            print("Jebb")
    else:
        print("Neibb")
