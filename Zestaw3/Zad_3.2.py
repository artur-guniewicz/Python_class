# a)

# L = [3, 5, 4] ; L = L.sort()

# Funkcja sort() niczego nie zwraca, sluzy do posortowania listy, dla ktorej zostala wywolana
# poprawiona wersja:

L = [3, 5, 4]
L.sort()
print(L)

# b)

# x, y = 1, 2, 3

# zbyt malo zmiennych / zbyt duzo wartosci
# poprawiona wersja:

x, y, z = 1, 2, 3
print(x, y, z)

# c)

# X = 1, 2, 3 ; X[1] = 4

# Tuple jest obiektem niemodyfikowalnym, nie można zmienić jego stanu
# poprawiona wersja:

X = 1, 2, 3
X = X[0], 4, X[2]
print(X)

# d)

# X = [1, 2, 3] ; X[3] = 4

# Wystepuje tu proba przypisania wartosci poza zakres listy
# poprawiona wersja:

X = [1, 2, 3]
X[2] = 4
print(X)

# e)

# X = "abc" ; X.append("d")

# Na obiektach typu string nie mozna uzyc metody append()
# poprawiona wersja:

X = "abc"
X += "d"
print(X)


# f)

# L = list(map(pow, range(8)))

# Funkcja pow() przyjmuje dwa argumenty, natomiast do funkcji map() mozna przekazac
# tylko funkcje ktore przyjmuja jeden argument
# poprawiona wersja:

def pow2(a):
    return a ** 2


L = list(map(pow2, range(8)))
print(L)
