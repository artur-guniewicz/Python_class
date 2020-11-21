import unittest
from Zestaw6.times import *


class TestTime(unittest.TestCase):

    def setUp(self):
        pass

    def test_print(self):
        self.assertEqual(str(Time(1)), "00:00:01")
        self.assertEqual(repr(Time(1)), "Time(1)")

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))

    def test_cmp(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertTrue(Time(2) >= Time(2))
        self.assertTrue(Time(3) >= Time(2))

    def test_int(self):
        self.assertEqual(int(Time(3600)), 3600)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
