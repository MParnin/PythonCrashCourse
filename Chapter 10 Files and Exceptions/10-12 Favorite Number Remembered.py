import json


def get_fav_number():
    filename = 'fav_number.json'
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number


def get_new_number():
    fav_number = input("What is your favorite number?")
    filename = 'fav_number.json'
    with open(filename, 'w') as f:
        json.dump(fav_number, f)


def greet_user():
    fav_number = get_fav_number()
    if fav_number:
        print(f"Your favorite number is {fav_number}")
    else:
        fav_number = get_new_number()
        print(f"We'll remember your number, {fav_number}")


greet_user()

##################################################################################
# Answer:


# try:
#     with open('favorite_number.json') as f:
#         number = json.load(f)
# except FileNotFoundError:
#     number = input("What's your favorite number? ")
#     with open('favorite_number.json', 'w') as f:
#         json.dump(number, f)
#     print("Thanks, I'll remember that.")
# else:
#     print(f"I know your favorite number! It's {number}.")
