# Create a dictionary and print the value for key 'sarah'

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite programming language is {language}.")

###########################################################################################
# Print each key and value of dictionary for each entry

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

###########################################################################################
# Print only the keys from the dictionary containing keys & values

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# for name in favorite_languages.keys():
#     print(name.title())

###########################################################################################
# Print each key in dictionary and additionally print the value associated with specific keys inside the while loop

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}.")

###########################################################################################
# Check if a specific key exists in the dictionary

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

###########################################################################################
# Loop through dictionary in an order different than the order the keys & values were inserted

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for take the poll.")

###########################################################################################
# Loop through dictionary and print all values without printing the keys

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

###########################################################################################
# # Loop through dictionary and print all values without printing the keys, excluding duplicates

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

###########################################################################################
# Loop through dictionary and print all values without printing the keys, excluding duplicates

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
