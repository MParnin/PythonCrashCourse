# import json

# fav_number = input("What is your favorite number?")

# filename = 'fav_number.json'
# with open(filename, 'w') as f:
#     json.dump(fav_number, f)
#     print(f"We'll remember your number, {fav_number}")

import json

filename = 'fav_number.json'
with open(filename) as f:
    fav_number = json.load(f)
    print(f"Your favorite number is {fav_number}")


##############################################################
# Answer:

# import json

# number = input("What's your favorite number? ")

# with open('favorite_number.json', 'w') as f:
#     json.dump(number, f)
#     print("Thanks! I'll remember that.")


# import json

# with open('favorite_number.json') as f:
#     number = json.load(f)

# print(f"I know your favorite number! It's {number}.")
