import random


def preparation(N):
    no = []
    for i in range(0, N):
        no.append(i)
    return no


def a_random(N):
    no = preparation(N)
    random.shuffle(no)
    return no


def b_almost_sorted(N):
    no = preparation(N)
    for i in range(1, N):
        j = random.randint(i - 1, i)
        no[i], no[j] = no[j], no[i]
    return no


def c_reversed_almost_sorted(N):
    no = b_almost_sorted(N)
    no.reverse()
    return no


def d_gaussian(N):
    no = []
    for i in range(N):
        no.append(random.gauss(0, 1))
    return no


def e_repeating(N):
    no = []
    for i in range(N):
        no.append(random.randint(0, N // 2))
    random.shuffle(no)
    return no
