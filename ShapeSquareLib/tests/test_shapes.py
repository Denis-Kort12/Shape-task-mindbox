import math
import unittest

from src.square_shapes.square_shapes import Circle, Triangle

class TestShapeSquare(unittest.TestCase):

    def test_circle_square(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.calculate_square(), math.pi, places=4)

    def test_triangle_square(self):
        triangle = Triangle(8,15,17)
        self.assertAlmostEqual(triangle.calculate_square(), 60.0)

    def test_triangle_right(self):
        triangle = Triangle(8,15,17)
        self.assertTrue(triangle.is_right())

    def test_triangle_right_side_chaos(self):
        triangle = Triangle(15,8,17)
        self.assertTrue(triangle.is_right())

    def test_triangle_no_right_side(self):
        triangle = Triangle(15,8,16)
        self.assertFalse(triangle.is_right())

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(2,3, 1000)
        with self.assertRaises(ValueError):
            Triangle(0, 8, 16)
        with self.assertRaises(ValueError):
            Triangle(-1, 8, 16)


if __name__ == "__main__":
    unittest.main()
