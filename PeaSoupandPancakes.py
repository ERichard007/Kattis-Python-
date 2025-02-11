restaraunts = {}

x = int(input())

for i in range(x):
    menu_items = int(input())
    rest_name = str(input())

    for y in range(menu_items):
        item = str(input())
        restaraunts[item] = rest_name 

for item, name in restaraunts.items():
    if (item == "pea soup") || (item == "pancakes")
