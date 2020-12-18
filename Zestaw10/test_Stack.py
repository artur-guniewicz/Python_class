from stack import *
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_str(self):
        self.assertEqual(str(self.stack), '[]')

    def test_eq(self):
        self.assertEqual(self.stack, Stack())

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.stack.is_full(), False)

    def test_pop(self):
        with self.assertRaises(ValueError):
            Stack().pop()
        self.stack.push(31)
        self.assertEqual(self.stack.pop(), 31)

    def test_push(self):
        self.stack.push(15)
        self.stack.push(18)
        self.stack.push(21)
        self.assertEqual(self.stack, Stack([15, 18, 21]))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
