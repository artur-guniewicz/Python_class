import unittest
from Zestaw7.rectangles import Rectangle
from Zestaw7.points import Point


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_rect(self):
        self.assertRaises(ValueError, Rectangle, 8, 8, 0, 0)

    def test_print(self):
        self.assertEqual(str(Rectangle(0, 0, 8, 4)), "[(0, 0), (8, 4)]")
        self.assertEqual(repr(Rectangle(0, 0, 8, 4)), "Rectangle(0, 0, 8, 4)")

    def test_cmp_rect(self):
        self.assertTrue(Rectangle(0, 0, 8, 4) == Rectangle(0, 0, 8, 4))
        self.assertTrue(Rectangle(0, 0, 8, 4) != Rectangle(0, 0, 1, 2))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 8, 4).center(), Point(4, 2))

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 8, 4).move(1, 1), Rectangle(1, 1, 9, 5))

    def test_intersection(self):
        """intersection test"""
        self.assertEqual(Rectangle(0, 0, 8, 4).intersection(Rectangle(4, 1, 12, 3)), Rectangle(4, 1, 8, 3))
        """no intersection test"""
        self.assertEqual(Rectangle(0, 0, 8, 4).intersection(Rectangle(9, 5, 10, 11)), None)

    def test_cover(self):
        self.assertEqual(Rectangle(0, 0, 8, 4).cover(Rectangle(4, 1, 12, 3)), Rectangle(0, 0, 12, 4))

    def test_make4(self):
        self.assertEqual(Rectangle(0, 0, 8, 4).make4(), [Rectangle(0, 0, 4, 2), Rectangle(4, 0, 8, 2), Rectangle(0, 2, 4, 4), Rectangle(4, 2, 8, 4)])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
