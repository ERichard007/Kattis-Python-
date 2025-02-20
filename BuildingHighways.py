numOfCities = int(input())
cityCrime = [int(x) for x in input().split()]
highways = [2000001]*(numOfCities-1)

for city in range(numOfCities):
    for crime in range(city+1, numOfCities):
        crimeRate = cityCrime[city] + cityCrime[crime]
        print(crimeRate)
        if (crimeRate < highways[crime-1]):
            highways[crime-1] = crimeRate
            print(highways)
            

print(sum(highways))
