rows, columns, classes = map(int, input().split())

grid = []

for x in range(rows):
    grid.append(input())

transposeGrid = list(map(list, zip(*grid)))
combos = set()

for x in range(1, len(transposeGrid)):
    combos.add([transposeGrid[x]])



print(grid)
print(transposeGrid)
print(combos)

