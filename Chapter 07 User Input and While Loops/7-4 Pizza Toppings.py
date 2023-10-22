prompt = "\nEnter a topping for your pizza:"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")

###################################################################
# Answer:

# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"  I'll add {topping} to your pizza.")
#     else:
#         break
