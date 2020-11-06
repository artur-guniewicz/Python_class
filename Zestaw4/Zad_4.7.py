result = []


def flatten(sequence):
    for i in sequence:
        if isinstance(i, (list, tuple)):
            flatten(i)
        else:
            result.append(i)

    return result


sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]

print('Sequence: ', sequence)
print('List of elements in sequence: ', flatten(sequence))
