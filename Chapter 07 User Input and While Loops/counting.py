# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#################################################################
# Adding a continue statment to code above to print only odd numbers.

current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)