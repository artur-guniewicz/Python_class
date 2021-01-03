import random


def preparation(n, k):
    L = []
    for i in range(n):
        L.append(random.randint(0, k - 1))
    L.sort()
    return L


def binary_rec(elements, left, right, searched_value):
    if right >= left:
        mid = left + (right - left) // 2
        if elements[mid] == searched_value:
            return mid
        if elements[mid] > searched_value:
            return binary_rec(elements, left, mid - 1, searched_value)
        return binary_rec(elements, mid + 1, right, searched_value)
    return -1


no = preparation(10, 100)
print('Random sorted list:', no)
searched_no = no[random.randint(0, len(no) - 1)]
print('Searched value', searched_no)
print('First occurrence in position:', binary_rec(no, 0, len(no), searched_no))
