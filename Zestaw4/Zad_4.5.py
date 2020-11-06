def reverse_iterative(list, left, right):
    counter = 0

    for i in range(left, right + 1):

        if counter >= (right - left + 1) / 2:
            break

        list[i], list[right - counter] = list[right - counter], list[i]

        counter += 1


def reverse_recursive(list, left, right):
    if left == right:
        return list

    list[left], list[right] = list[right], list[left]

    return reverse_recursive(list, left + 1, right - 1)


list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('List: ', list_1)


reverse_iterative(list_1, 2, 8)
print('Iterative reversion between 2nd and 8th element: ', list_1)

reverse_recursive(list_2, 3, 7)
print('Recursive reversion between 2nd and 8th element: ', list_2)


