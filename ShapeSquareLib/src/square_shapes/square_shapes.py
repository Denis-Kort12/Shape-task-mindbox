import math
from abc import ABC, abstractmethod
from itertools import combinations

class Shape(ABC):

    @abstractmethod
    def calculate_square(self):
        pass

class Circle(Shape):

    def __init__(self, radius):

        if radius <= 0:
            raise ValueError("Incorrect radius (<=0)")

        self.radius = radius

    def calculate_square(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):

    def __init__(self, first_side, second_side, third_side):

        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

        if first_side <= 0 or second_side <= 0 or third_side <= 0:
            raise ValueError("Sides no positive (triangle)")
        if not self._is_valid():
            raise ValueError("Invalid sides (triangle)")

    def calculate_square(self):
        half_perimeter = (self.first_side + self.second_side + self.third_side)/2

        return math.sqrt(
            half_perimeter*
            (half_perimeter-self.first_side)*
            (half_perimeter-self.second_side)*
            (half_perimeter-self.third_side)
        )

    def is_right(self):
        list_sides = [self.first_side, self.second_side, self.third_side]
        list_sides.sort()

        return math.isclose(list_sides[0]**2 + list_sides[1]**2, list_sides[2]**2, rel_tol=1e-9)

    def _is_valid(self):
        a, b, c = self.first_side, self.second_side, self.third_side
        return (a + b > c) and (a + c > b) and (b + c > a)
