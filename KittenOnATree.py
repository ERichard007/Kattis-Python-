kittenBranch = int(input())

myTree = {}
while True:
    branch = input().split()
    
    if (int(branch[0]) == -1): break

    value = int(branch[0])
    
    for i in range(1, len(branch), 1):
        myTree[int(branch[i])] = value

pathway = []
while True:
    newbranch = myTree.get(kittenBranch)

    if newbranch:
        pathway.append(kittenBranch)
        kittenBranch = newbranch
        
    else:
        break

pathway.append(kittenBranch)

for x in pathway: print(x, end=" ")
