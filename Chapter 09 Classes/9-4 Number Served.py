class Restaurant:
    def __init__(self, name, cuisine_type):
        """Initialize name and age attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.name} is the name.")

        print(f"\n{self.cuisine_type} is the type of food.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, inc):
        self.number_served += inc


restaurant = Restaurant('Ginos', 'Italian')

print(f"{restaurant.name}")

print(f"{restaurant.cuisine_type}")

print(f"{restaurant.number_served}")

restaurant.number_served = 15

print(f"{restaurant.number_served}")

restaurant.describe_restaurant()

restaurant.open_restaurant()

restaurant.set_number_served(19)

print(f"{restaurant.number_served}")

restaurant.increment_number_served(6)

print(f"{restaurant.number_served}")

########################################################################################
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


# restaurant = Restaurant('the mean queen', 'pizza')
# restaurant.describe_restaurant()

# print(f"\nNumber served: {restaurant.number_served}")
# restaurant.number_served = 430
# print(f"Number served: {restaurant.number_served}")

# restaurant.set_number_served(1257)
# print(f"Number served: {restaurant.number_served}")

# restaurant.increment_number_served(239)
# print(f"Number served: {restaurant.number_served}")
