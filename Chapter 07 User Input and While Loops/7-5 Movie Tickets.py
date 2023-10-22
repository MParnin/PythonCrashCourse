prompt = "\nEnter age for movie ticket price:"

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    if age < '3':
        print("\n Ticket is free.")
    if age > '3' and age < '12':
        print("\n Ticket is $10.")
    if age > '12':
        print("\n Ticket is $15.")

#########################################################################
# Answer:

# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")
