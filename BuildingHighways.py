from heapq import heappush, heappop

numCities = int(input())
cityCrime = list(map(int, input().split()))

cityAndCrime = []
Visited = [False]*numCities
cost = 0

if numCities == 1:
    print(cost)
else:
    heappush(cityAndCrime, (0,0))
    
    while cityAndCrime:
    
        city, crime = heappop(cityAndCrime)




