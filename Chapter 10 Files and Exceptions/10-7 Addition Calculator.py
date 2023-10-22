print("Give me two numbers, and I'll add them.")
print("Enter 'q' ti quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second Number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add text")
    else:
        print(answer)

###################################################################################
# Answer:

# print("Enter 'q' at any time to quit.\n")

# while True:
#     try:
#         x = input("\nGive me a number: ")
#         if x == 'q':
#             break

#         x = int(x)

#         y = input("Give me another number: ")
#         if y == 'q':
#             break

#         y = int(y)

#     except ValueError:
#         print("Sorry, I really needed a number.")

#     else:
#         sum = x + y
#         print(f"The sum of {x} and {y} is {sum}.")
