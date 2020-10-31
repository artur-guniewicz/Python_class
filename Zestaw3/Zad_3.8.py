squence1 = [0, 1, 2, 3, 4, 5, 6]
squence2 = [5, 6, 7, 8, 9]

print('First squence: ', squence1)
print('Second squence: ', squence2)

# a)

same = set()

for i in squence1:
    for j in squence2:
        if i == j:
            same.add(i)

print('Same elements: ', same)

# b)

all = set(squence1).union(squence2)

print('All elements: ', all)