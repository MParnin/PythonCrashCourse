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
    print("File not found")

################################################################
# Answer:

# filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:
#     print(f"\nReading file: {filename}")
#     try:
#         with open(filename) as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         print("  Sorry, I can't find that file.")
