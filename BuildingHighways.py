from heapq import heappush, heappop

numCities = int(input())
cityCrime = list(map(int, input().split()))

crimeAndCity = []

notVisited = set(range(numCities))
minCrime = [2000001]*numCities

minCrime[0] = 0
cost = 0

if numCities == 1:
    print(cost)
else:
    heappush(crimeAndCity, (0,0))
    while crimeAndCity:
        crime, city = heappop(crimeAndCity)
        
        if city not in notVisited: continue

        notVisited.remove(city)
        cost += crime

        for neighbor in notVisited:
            if neighbor != city:
                newCrime = cityCrime[city] + cityCrime[neighbor]
                if newCrime < minCrime[neighbor]:
                    minCrime[neighbor] = newCrime
                    heappush(crimeAndCity, (newCrime, neighbor))
    print(cost)




