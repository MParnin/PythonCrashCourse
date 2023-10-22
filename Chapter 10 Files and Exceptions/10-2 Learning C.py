filename = '10-2.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.replace('Python', 'Solidity'))
