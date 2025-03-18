availableComponents, typesOfComponents, moneyAvailable = list(map(int, input().split()))

a = input().split()
componentNames = {a[x] : [] for x in range(typesOfComponents)}

lowPerf = 0
highPerf = 0
for x in range(availableComponents):
    a = input().split()
    highPerf = max(highPerf, int(a[2]))
    componentNames[a[0]].append((int(a[1]), int(a[2])))

print(f"{componentNames} + {highPerf}")