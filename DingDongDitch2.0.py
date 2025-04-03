houses, friends = map(int, input().split())
angerLevels = list(map(int, input().split()))
housesCanRing = list(map(int, input().split()))

angerLevels.sort()
sum = 0
for i in range(houses):
    sum += angerLevels[i]
    angerLevels[i] = sum

for i in range(friends):
    canRing = housesCanRing[i]
    print(angerLevels[canRing-1])
        


