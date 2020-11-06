def sum_seq(sequence):
    sum = 0

    for i in sequence:
        if isinstance(i, (list, tuple)):
            sum += sum_seq(i)
        else:
            sum += i

    return sum


sequence = [(1, 2), [], 3, 4, [5, (6, 7)], [], (8, 9)]

print('Sequence: ', sequence)
print('Sum of elements in sequence: ', sum_seq(sequence))