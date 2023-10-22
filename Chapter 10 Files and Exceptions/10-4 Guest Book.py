from tkinter import N


filename = 'guest_book.txt'

guest_polling = True

with open(filename, 'a') as file_object:
    while guest_polling:
        guest_name = input("What is your name?")
        if guest_name == 'q':
            guest_polling = False
        else:
            print(f"Hello {guest_name.title()}")
            file_object.write(f"{guest_name}\n")
