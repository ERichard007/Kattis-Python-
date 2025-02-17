from collections import defaultdict

numOfCities = int(input())
cityCrime = [int(x) for x in input().split()]

cityHighways = defaultdict(int)

city = -1
while True:
    city += 1
    if city >= numOfCities: break 
    cityCost = cityCrime[city]
    for x in range(1+city, numOfCities):
        highwayCost = cityCost + cityCrime[x] 
        if (highwayCost < cityHighways[x+1] or cityHighways[x+1] == 0):
            cityHighways[x+1] = highwayCost

print(sum(cityHighways.values()))