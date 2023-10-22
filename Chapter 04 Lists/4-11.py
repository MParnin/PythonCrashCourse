favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("supreme")

friend_pizzas.append("bacon")

# Print the names of all the pizzas.
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# print("\n")

# Print a sentence about each pizza.
# for pizza in favorite_pizzas:
#    print("I really love " + pizza + " pizza!")

#print("\nI really love pizza!")
