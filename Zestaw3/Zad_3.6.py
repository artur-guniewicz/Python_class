height = int(input('Enter height: '))
length = int(input('Enter length: '))

output = '\n'

for i in range(height * 2 + 1):
    if i % 2 == 0:
        output += '+'
        for j in range(length):
            output += '---+'
        output += '\n'
    else:
        output += "|"
        for j in range(length):
            output += '   |'
        output += '\n'

print(output)
