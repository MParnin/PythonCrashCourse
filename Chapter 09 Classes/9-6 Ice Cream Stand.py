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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ('chocolate', 'vanilla', 'strawberry')

    def print_flavors(self):
        print(f"The flavors are: {self.flavors}")


ice_cream_stand = IceCreamStand('mikes', 'dessert')

ice_cream_stand.print_flavors()

#######################################################################
# Answer:

# class Restaurant():
#     """A class representing a restaurant."""

#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = f"{self.name} serves wonderful {self.cuisine_type}."
#         print(f"\n{msg}")

#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = f"{self.name} is open. Come on in!"
#         print(f"\n{msg}")

#     def set_number_served(self, number_served):
#         """Allow user to set the number of customers that have been served."""
#         self.number_served = number_served

#     def increment_number_served(self, additional_served):
#         """Allow user to increment the number of customers served."""
#         self.number_served += additional_served


# class IceCreamStand(Restaurant):
#     """Represent an ice cream stand."""

#     def __init__(self, name, cuisine_type='ice_cream'):
#         """Initialize an ice cream stand."""
#         super().__init__(name, cuisine_type)
#         self.flavors = []

#     def show_flavors(self):
#         """Display the flavors available."""
#         print("\nWe have the following flavors available:")
#         for flavor in self.flavors:
#             print(f"- {flavor.title()}")


# big_one = IceCreamStand('The Big One')
# big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

# big_one.describe_restaurant()
# big_one.show_flavors()
