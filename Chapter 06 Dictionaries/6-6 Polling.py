favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah', 'john']
for name in friends:
    if name in favorite_languages.keys():
        print(f"\t{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take the poll")

###########################################################################################
# Answer:

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# print("\n")

# coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
# for coder in coders:
#     if coder in favorite_languages.keys():
#         print(f"Thank you for taking the poll, {coder.title()}!")
#     else:
#         print(f"{coder.title()}, what's your favorite programming language?")
