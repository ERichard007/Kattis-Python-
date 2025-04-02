import heapq #Not fast enough

houses, friends = map(int, input().split())
angerLevels = list(map(int, input().split()))
housesCanRing = list(map(int, input().split()))

heapq.heapify(angerLevels)

print(f"** {houses} {friends} {angerLevels} {housesCanRing} **\n")

for x in range(friends):
    canRing = housesCanRing[x]
    deleted = []

    sum = 0
    for y in range(canRing):
        angry = heapq.heappop(angerLevels)
        sum += angry
        deleted.append(angry)
        
    print(sum)
    
    for anger in deleted:
        heapq.heappush(angerLevels, anger)

