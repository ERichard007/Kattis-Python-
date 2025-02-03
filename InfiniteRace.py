racers = int(input()) #racers
num_of_events = int(input()) #number of events

event_dict = {} #dictionary to hold each racer and how many times they've been passed

for i in range(num_of_events):
    #print(f"DICT: {event_dict}")
    event = int(input())

    if event > 0:
        if (event not in event_dict):
            event_dict[event] = 0
        else:
            event_dict[event] += 1

            mark_keys = []

            for key, value in event_dict.items():
                if value == 0:
                    mark_keys.append(key)
            
            for key in mark_keys:
                event_dict.pop(key)
    
    else:
        event = abs(event)
        if (event not in event_dict):
            continue
        else:
            if (event_dict[event] == 0):
                event_dict.pop(event)
            else:
                event_dict[event] -= 1

sum = 0
for val in event_dict.values():
    sum += val

#print(f"DICT: {event_dict}")
print(sum)

