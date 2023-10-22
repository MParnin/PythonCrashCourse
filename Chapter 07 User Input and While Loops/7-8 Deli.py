sandwich_orders = ['italian', 'cbr', 'meatball']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nMaking: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

###################################################################
# Answer:

# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")
