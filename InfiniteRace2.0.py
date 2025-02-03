#I DID IT THANK GOD, IT WAS SUPPOSED TO BE EASY THEY SAID

racers = int(input()) #racers
num_of_events = int(input()) #number of events
laps = 0 #number of laps

passed_racers = {} #a dictionary of passed racers, key = racer, value = times passed

for i in range(num_of_events):
    event = int(input())

    if abs(event) not in passed_racers:
        passed_racers[abs(event)] = 0
    
    if event > 0:
        passed_racers[event] += 1

        if passed_racers[event] > 1:
            laps+=1
            marked = []

            for x,y in passed_racers.items():
                if (y>1):
                    passed_racers[x] = 1
                else:
                    marked.append(x)
            
            for delete in marked:
                passed_racers.pop(delete)
    else:
        event = abs(event)

        if (passed_racers[event] > 0):
            passed_racers[event] -= 1
            
print(laps)