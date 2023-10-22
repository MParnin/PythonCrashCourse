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

################################################################################
# Answer:

# try:
#     x = input("Give me a number: ")
#     x = int(x)

#     y = input("Give me another number: ")
#     y = int(y)
# except ValueError:
#     print("Sorry, I really needed a number.")
# else:
#     sum = x + y
#     print(f"The sum of {x} and {y} is {sum}.")
