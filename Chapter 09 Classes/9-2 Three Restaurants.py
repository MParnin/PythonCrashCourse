class Restaurant:
    def __init__(self, name, cuisine_type):
        """Initialize name and age attributes."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.name} is the name.")

        print(f"\n{self.cuisine_type} is the type of food.")

    def open_restaurant(self):
        print("The restaurant is open.")


restaurant1 = Restaurant('Ginos', 'Italian')

restaurant2 = Restaurant('Sals', 'Pizza')

restaurant3 = Restaurant('Outback', 'steak')


restaurant1.describe_restaurant()

restaurant2.describe_restaurant()

restaurant3.describe_restaurant()

####################################################################################
# Answer:

# class Restaurant():
#     """A class representing a restaurant."""

#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = f"{self.name} serves wonderful {self.cuisine_type}."
#         print(f"\n{msg}")

#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = f"{self.name} is open. Come on in!"
#         print(f"\n{msg}")

# mean_queen = Restaurant('the mean queen', 'pizza')
# mean_queen.describe_restaurant()

# ludvigs = Restaurant("ludvig's bistro", 'seafood')
# ludvigs.describe_restaurant()

# mango_thai = Restaurant('mango thai', 'thai food')
# mango_thai.describe_restaurant()
