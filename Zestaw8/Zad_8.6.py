class Solver:
    initial = {(0, 0): 0.5, (0, 1): 1, (1, 0): 0}

    def __init__(self):

        self.initial = {(0, 0): 0.5, (0, 1): 1, (1, 0): 0}

    def dynamic(self, i, j):
        if (i, j) in self.initial.keys():
            return self.initial.get((i, j))
        if i == 0:
            return self.initial.get((0, 1))
        if j == 0:
            return self.initial.get((1, 0))
        if i > 0 and j > 0:
            self.initial[(i, j)] = 0.5 * (self.dynamic(i - 1, j) + self.dynamic(i, j - 1))
            return self.initial.get((i, j))


def recursive(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (recursive(i - 1, j) + recursive(i, j - 1))


print("Obliczenie wartości funkcji P(i, j); i = 2, j = 3")

print(" -> dynamicznie: ", Solver().dynamic(2, 3))
print(" -> rekurencyjnie: ", recursive(2, 3))
