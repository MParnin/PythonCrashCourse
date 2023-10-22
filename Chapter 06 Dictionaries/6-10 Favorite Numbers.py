fav_numbers = {
    'Mike': ['55', '21'],
    'Michaela': ['4', '7'],
    'Andy': ['41', '99'],
    'Steve': ['1', '2'],
    "Joe": ['2', '3']
}

for name, numbers in fav_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"- {number}")

###########################################################################################
# Answer:

# favorite_numbers = {
#     'mandy': [42, 17],
#     'micah': [42, 39, 56],
#     'gus': [7, 12],
#     }

# for name, numbers in favorite_numbers.items():
#     print(f"\n{name.title()} likes the following numbers:")
#     for number in numbers:
#         print(f"  {number}")
