personal_info1 = {
    'first_name': "Mike",
    'last_name': "P",
    'age': '35',
    'location': 'VA',
}

personal_info2 = {
    'first_name': "Michaela",
    'last_name': "P",
    'age': '32',
    'location': 'VA',
}

personal_info3 = {
    'first_name': "Todd",
    'last_name': "S",
    'age': '57',
    'location': 'VA',
}

peoples = [personal_info1, personal_info2, personal_info3]

for people in peoples:
    print(people)

#############################################################################
# Answer:

# # Make an empty list to store people in.
# people = []

# # Define some people, and add them to the list.
# person = {
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 46,
#     'city': 'sitka',
#     }
# people.append(person)

# person = {
#     'first_name': 'lemmy',
#     'last_name': 'matthes',
#     'age': 2,
#     'city': 'sitka',
#     }
# people.append(person)

# person = {
#     'first_name': 'willie',
#     'last_name': 'matthes',
#     'age': 11,
#     'city': 'sitka',
#     }
# people.append(person)

# # Display all of the information in the dictionary.
# for person in people:
#     name = f"{person['first_name'].title()} {person['last_name'].title()}"
#     age = person['age']
#     city = person['city'].title()

#     print(f"{name}, of {city}, is {age} years old.")
