filename1 = ('cats.txt')

filename2 = ('dogs.txt')

try:
    with open(filename1) as c:
        lines1 = c.readlines()
        for line in lines1:
            print(line.strip())

    with open(filename2) as d:
        lines2 = d.readlines()
        for line in lines2:
            print(line.strip())

except FileNotFoundError:
    pass

#######################################################
# Answer:

# filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:

#     try:
#         with open(filename) as f:
#             contents = f.read()

#     except FileNotFoundError:
#         pass

#     else:
#         print(f"\nReading file: {filename}")
#         print(contents)
