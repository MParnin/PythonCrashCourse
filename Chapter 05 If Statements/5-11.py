
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers[0:3]:
    if number == 1:
        print(f"{number}st")
    if number == 2:
        print(f"{number}nd")
    if number == 3:
        print(f"{number}rd")

for number in numbers[3:]:
    print(f"{number}th")

# Solution
#numbers = list(range(1,10))

# for number in numbers:
#    if number == 1:
#        print("1st")
#    elif number == 2:
#        print("2nd")
#    elif number == 3:
#        print("3rd")
#    else:
#        print(f"{number}th")
