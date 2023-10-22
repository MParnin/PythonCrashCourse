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


class Admin(User):
    def __init__(self, first_name, last_name, location, age, employment):
        super().__init__(first_name, last_name, location, age, employment)

        self.show_privileges = Privileges()


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print({self.privileges})


admin = Admin('Mike', 'P', 'Suffolk', 35, 'Engineer')

admin_privileges = ['can add post',
                    'can delete post',
                    'can ban user',
                    ]
admin.privileges.privileges = admin_privileges

admin.show_privileges()

####################################################################################
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
#         self.login_attempts = 0

#     def describe_user(self):
#         """Display a summary of the user's information."""
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"  Username: {self.username}")
#         print(f"  Email: {self.email}")
#         print(f"  Location: {self.location}")

#     def greet_user(self):
#         """Display a personalized greeting to the user."""
#         print(f"\nWelcome back, {self.username}!")

#     def increment_login_attempts(self):
#         """Increment the value of login_attempts."""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """Reset login_attempts to 0."""
#         self.login_attempts = 0


# class Admin(User):
#     """A user with administrative privileges."""

#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the admin."""
#         super().__init__(first_name, last_name, username, email, location)

#         # Initialize an empty set of privileges.
#         self.privileges = Privileges()


# class Privileges():
#     """A class to store an admin's privileges."""

#     def __init__(self, privileges=[]):
#         self.privileges = privileges

#     def show_privileges(self):
#         print("\nPrivileges:")
#         if self.privileges:
#             for privilege in self.privileges:
#                 print(f"- {privilege}")
#         else:
#             print("- This user has no privileges.")


# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()

# eric.privileges.show_privileges()

# print("\nAdding privileges...")
# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
# ]
# eric.privileges.privileges = eric_privileges
# eric.privileges.show_privileges()
