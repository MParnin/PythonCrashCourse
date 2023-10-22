# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

################################################################################
# Adding a loop to the function to describe what is being done.

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

#################################################################################
# Mixing positional and arbitrary arguments

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#################################################################################
# Making function a module

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")