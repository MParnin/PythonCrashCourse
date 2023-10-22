# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

###########################################################
# Reading line by line

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

###########################################################
# Making a list of the lines read from the file

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

#############################################################
# Working with a files contents

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
