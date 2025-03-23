availableComponents, typesOfComponents, moneyAvailable = list(map(int, input().split()))

a = input().split()
componentNames = {a[x] : [] for x in range(typesOfComponents)}

lowPerf = 0
highPerf = 0
for x in range(availableComponents):
    a = input().split()
    highPerf = max(highPerf, int(a[2]))
    componentNames[a[0]].append((int(a[1]), int(a[2])))

bestPerf = -1
while lowPerf <= highPerf:
    budget = moneyAvailable
    midPerf = lowPerf + (highPerf - lowPerf) // 2
    print(midPerf)

    possible = True
    for comp, priceAndPerf in componentNames.items():
        minPrice = float('inf')
        for price, perf in priceAndPerf:
            if perf >= midPerf:
                minPrice = min(minPrice, price)

        if minPrice == float('inf'):
            possible = False
            break
        else:
            budget -= minPrice

    if possible and budget >= 0:
        lowPerf = midPerf + 1
        bestPerf = midPerf
    else:
        highPerf = midPerf - 1

if bestPerf != -1:
    print(bestPerf)
else:
    print("O nei!")

    
            

        