import random


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
        n oznacza liczbę losowanych punktów."""

    nb_pi = 0
    random.getstate()

    points_from_sqaure = 0
    points_from_circle = 0

    for i in range(n):

        random1 = random.random()
        random2 = random.random()

        distance = (random1 * random1) + (random2 * random2)

        if distance <= 1:
            points_from_circle = points_from_circle + 1

        points_from_sqaure = points_from_sqaure + 1

        nb_pi = 4.0 * points_from_circle / points_from_sqaure

    return nb_pi


print('Liczba pi:')
print(calc_pi(182410))