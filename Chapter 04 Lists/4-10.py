foods = ['pizza', 'falafel', 'carrot cake',
         'cannoli', 'ice cream', 'spaghetti', 'filler1', 'filler2', 'filler3']
print("The first three items in my list are:")
for food in foods[:3]:
    print(food.title())

print("The middle three items in my list are:")
for food in foods[3:6]:
    print(food.title())

print("The last three items in my list are:")
for food in foods[6:]:
    print(food.title())
