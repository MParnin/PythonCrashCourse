def make_sandwich(*ingreds):
    print("\nAdding the following to the sandwich:")
    for ingred in ingreds:
        print(f"- {ingred}")


make_sandwich('bacon', 'black olives', 'provolone')

make_sandwich('bacon', 'black olives')

make_sandwich('bacon')

################################################################
# Answer:

# def make_sandwich(*items):
#     """Make a sandwich with the given items."""
#     print("\nI'll make you a great sandwich:")
#     for item in items:
#         print(f"  ...adding {item} to your sandwich.")
#     print("Your sandwich is ready!")

# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')
