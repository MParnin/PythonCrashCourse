sandwich_orders = ['italian', 'pastrami',
                   'cbr', 'pastrami', 'meatball', 'pastrami']

finished_sandwiches = []

print("The deli has run out of pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nMaking: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

################################################################################
# Answer:

# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []

# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print("\n")
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")
