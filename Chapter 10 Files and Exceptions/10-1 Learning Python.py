filename = '10-1.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    lines = file_object.readlines()

file_contents = ''

for line in lines:
    file_contents += line

print(file_contents)
