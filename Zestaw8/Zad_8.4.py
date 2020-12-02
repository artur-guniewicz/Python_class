import math


def triangle_condition(a, b, c):
    triangle_sides = [a, b, c]

    longest_index = triangle_sides.index(max(triangle_sides))
    longest_side = triangle_sides[longest_index]
    triangle_sides.pop(longest_index)

    return longest_side < triangle_sides[0] + triangle_sides[1]


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
       Herona. Długości boków trójkąta wynoszą a, b, c."""

    if not triangle_condition(a, b, c):
        raise ValueError("Podane boki nie spełniają warunków trójkąta")

    p = (a + b + c) / 2  # half of circuit

    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print("Boki spełniające warunki trójkąta: (9, 12, 18)")
print("Pole =", heron(9, 12, 18))
print('')
print("Boki niespełniające warunków trójkąta: (9, 12, 32):")
print(heron(9, 12, 32))
