rows, columns, classes = map(int, input().split())

grid = []

for x in range(rows):
    grid.append(input())

transposeGrid = list(map(list, zip(*grid)))
sets = [set(sublist) for sublist in transposeGrid]

combos = []

for s in sets:
    matched = False
    for c in combos:
        if s & c:
            c.update(s)
            matched = True
            break
    if not matched:
        combos.append(s)


print(len(combos))

#honestly some powerful stuff sets can do, fun to use