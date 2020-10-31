size = int(input('Enter size: '))

output = '\n| '

for i in range(size):
    output += '. . . . | '

output += '\n0'

for i in range(size):
    nb = str(i + 1)
    nbs = ''.ljust(10 - len(nb), ' ') + nb
    output += nbs

print(output)
