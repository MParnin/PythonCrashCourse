class User:
    def __init__(self, first_name, last_name, location, age, employment):
        """Initialize name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.employment = employment

    def describe_user(self):
        print(f"{self.last_name}, {self.first_name} is located in {self.location}, is {self.age} years old and is a {self.employment}")

    def greet_user(self):
        print(f"Hello {self.first_name}")


p1 = User('Mike', 'P', 'Suffolk', 35, 'Engineer')
p2 = User('Michaela', 'P', 'Suffolk', 32, 'Realtor')

p1.describe_user()
p2.describe_user()

p1.greet_user()
#############################################################################
# Answer:

# class User():
#     """Represent a simple user profile."""

#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the user."""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()

#     def describe_user(self):
#         """Display a summary of the user's information."""
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"  Username: {self.username}")
#         print(f"  Email: {self.email}")
#         print(f"  Location: {self.location}")

#     def greet_user(self):
#         """Display a personalized greeting to the user."""
#         print(f"\nWelcome back, {self.username}!")

# eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
# eric.greet_user()

# willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
# willie.describe_user()
# willie.greet_user()
