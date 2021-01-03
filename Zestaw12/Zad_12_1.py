import random


def preparation(n, k):
    L = []
    for i in range(n):
        L.append(random.randint(0, k - 1))
    return L


def linear_search(elements, searched_value):
    occurrences = []
    for i in range(len(elements)):
        if elements[i] == searched_value:
            occurrences.append(i)
    return occurrences


no = preparation(100, 10)
print('Random list:', no)
searched_no = no[random.randint(0, len(no) - 1)]
print('Searched random value:', searched_no)
print('Occurrences in positions:', linear_search(no, searched_no))
