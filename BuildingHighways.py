from heapq import heappush, heappop

numCities = int(input())
cityCrime = list(map(int, input().split()))

crimeAndCity = []
notVisited = [x for x in range(numCities)]
cost = 0

if numCities == 1:
    print(cost)
else:
    heappush(crimeAndCity, (0,0))
    while crimeAndCity:
        crime, city = heappop(crimeAndCity)
        if city not in notVisited: continue
        notVisited.pop(notVisited.index(city))
        cost += crime
        for neighbor in notVisited:
            heappush(crimeAndCity, (cityCrime[city]+cityCrime[neighbor], neighbor))
    print(cost)




