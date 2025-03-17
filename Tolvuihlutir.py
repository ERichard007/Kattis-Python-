availableComponents, typesOfComponents, moneyAvailable = list(map(int, input().split()))
a = input().split()
componentNames = {a[x] : [] for x in range(typesOfComponents)}

for x in range(availableComponents):
    a = input().split()
    componentNames[a[0]].append((int(a[1]), int(a[2])))

currentComp = {}
minPerf = float('inf')
for k, v in componentNames.items():
    component = componentNames[k]
    component.sort(key=lambda x: (int(x[1]), int(x[0])))

    if len(component) == 0 : 
        print("O nei!") 
        exit() 

    value = component[-1][0]
    performance = component[-1][1]
    index = len(component) - 1

    if moneyAvailable - value >= 0:
        print(f"BUYING {k} FOR {value} --> MONEY LEFT {moneyAvailable - value}")
        moneyAvailable -= value
        minPerf = min(minPerf, performance)

        if index-1 >= 0: currentComp[k] = [performance - int(component[index-1][1]), index]
    
    else:
        moneyNeeded = value - moneyAvailable
        while moneyNeeded > 0:
            print(f"NEED MONEY: {moneyNeeded} --> {currentComp}")

            if len(currentComp) == 0 :
                print("O nei!") 
                exit() 

            currentComp = dict(sorted(currentComp.items(), key = lambda item: item[1]))
            replaceComponent = list(currentComp.keys())[0]
            replacePerformance, replaceIndex = currentComp.pop(replaceComponent)

            moneyAvailable += (int(componentNames[replaceComponent][replaceIndex][0]) - int(componentNames[replaceComponent][replaceIndex-1][0]))
            moneyNeeded = max(0, value - moneyAvailable)
            minPerf = min(minPerf, int(componentNames[replaceComponent][replaceIndex-1][1]))

            print(f"BUYING {replaceComponent} FOR {componentNames[replaceComponent][replaceIndex-1][0]} --> MONEY LEFT {moneyAvailable} MONEY NEEDED {moneyNeeded}")

            if replaceIndex-1 >= 0: currentComp[replaceComponent] = [replacePerformance - int(componentNames[replaceComponent][replaceIndex-1][1]), replaceIndex-1]

print(minPerf)