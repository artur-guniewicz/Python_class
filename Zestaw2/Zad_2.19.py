L = [1, 2, 3, 11, 12, 13, 111, 122, 123]

result = ''

for num in L:
    result += str(num).zfill(3) + ' '

print(result.strip())