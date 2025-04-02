import heapq

houses, friends = map(int, input().split())
angerLevels = list(map(int, input().split()))
housesCanRing = list(map(int, input().split()))

heapq.heapify(angerLevels)
for x in range(len(angerLevels)):

print(f"** {houses} {friends} {angerLevels} {housesCanRing} **\n")



