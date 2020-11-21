import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Zwraca string '(x, y)'."""
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        """Zwraca string "Point(x, y)"""
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        """Obsługa point1 == point2"""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Obsługa point1 != point2"""
        return not self == other

    """Punkty jako wektory 2D."""
    def __add__(self, other):
        """V1 + V2"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """V1 - V2"""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """V1 * V2, iloczyn skalarny"""
        return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):
        """v1 x v2, iloczyn wektorowy 2D"""
        return self.x * other.y - self.y * other.x

    def length(self):
        """Długość wektora"""
        return math.sqrt(self.x**2 + self.y**2)