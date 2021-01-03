from Zestaw11.Zad_11_1 import *


def partition(no, beginning, end):
    mid = beginning + (end - beginning) // 2
    p = no[mid]

    while beginning <= end:
        while no[beginning] < p:
            beginning += 1
        while no[end] > p:
            end -= 1
        if beginning <= end:
            no[beginning], no[end] = no[end], no[beginning]
            beginning += 1
            end -= 1
    return beginning


def iterative_quicksort(no):
    beginning = 0
    end = len(no) - 1
    S = [beginning, end]

    while len(S) > 0:
        end = S.pop()
        beginning = S.pop()

        p_index = partition(no, beginning, end)

        if p_index - 1 > beginning:
            S.append(beginning)
            S.append(p_index - 1)

        if p_index < end:
            S.append(p_index)
            S.append(end)


print('a) random:')
no_list = a_random(10)
print(no_list)
iterative_quicksort(no_list)
print(no_list, '\n')

print('b) almost random:')
no_list = b_almost_sorted(10)
print(no_list)
iterative_quicksort(no_list)
print(no_list, '\n')

print('c) reversed almost random:')
no_list = c_reversed_almost_sorted(10)
print(no_list)
iterative_quicksort(no_list)
print(no_list, '\n')

print('d) gaussian:')
no_list = d_gaussian(10)
print(no_list)
iterative_quicksort(no_list)
print(no_list, '\n')

print('e) random, repeating and belonging to the collection \"k\":')
no_list = e_repeating(10)
print(no_list)
iterative_quicksort(no_list)
print(no_list, '\n')
