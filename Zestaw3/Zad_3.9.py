sequences = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

output = []

for i in sequences:
    output.append(sum(i))

print(output)