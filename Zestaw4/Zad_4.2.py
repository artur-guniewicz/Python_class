def draw_1(size):
    output = '\n| '

    for i in range(size):
        output += '. . . . | '

    output += '\n0'

    for i in range(size):
        nb = str(i + 1)
        nbs = ''.ljust(10 - len(nb), ' ') + nb
        output += nbs

    return output


def draw_2(height, length):
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

    return output


print('Drawing a measure')
size = int(input('Enter the size: '))
print(draw_1(size), '\n')

print('Drawing a rectangle')
height = int(input("Enter the height: "))
length = int(input("Enter the length: "))
print(draw_2(height, length))

