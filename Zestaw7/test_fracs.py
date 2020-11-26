import unittest
from Zestaw7.fracs import Frac


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = Frac()

    def test_create_frac(self):
        self.assertRaises(ValueError, Frac, 1, 0)

    def test_print(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")

    def test_cmp_frac(self):
        self.assertTrue(Frac(1, 2) < Frac(3, 4))
        self.assertTrue(Frac(1, 2) <= Frac(2, 4))
        self.assertTrue(Frac(3, 4) > Frac(1, 2))
        self.assertTrue(Frac(2, 4) >= Frac(1, 2))
        self.assertTrue(Frac(2, 4) == Frac(1, 2))
        self.assertTrue(Frac(1, 2) == Frac(1, 2))
        self.assertTrue(Frac(1, 2) != Frac(1, 3))

    def test_add_frac_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))

    def test_add_frac_int(self):
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))

    def test_add_int_frac(self):
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))

    def test_add_frac_float(self):
        self.assertEqual(Frac(1, 3) + 1.5, Frac(11, 6))

    def test_sub_frac_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))

    def test_sub_frac_int(self):
        self.assertEqual(Frac(1, 2) - 1, Frac(-1, 2))

    def test_sub_int_frac(self):
        self.assertEqual(1 - Frac(1, 2), Frac(1, 2))

    def test_sub_frac_float(self):
        self.assertEqual(Frac(2, 3) - 0.5, Frac(1, 6))

    def test_mul_frac_frac(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))

    def test_mul_frac_int(self):
        self.assertEqual(Frac(1, 3) * 2, Frac(2, 3))

    def test_mul_int_frac(self):
        self.assertEqual(2 * Frac(1, 3), Frac(2, 3))

    def test_mul_frac_float(self):
        self.assertEqual(Frac(2, 5) * 1.5, Frac(3, 5))

    def test_div_frac_frac(self):
        self.assertEqual(Frac(2, 3) / Frac(3, 4), Frac(8, 9))

    def test_div_frac_int(self):
        self.assertEqual(Frac(2, 3) / 2, Frac(1, 3))

    def test_div_int_frac(self):
        self.assertEqual(2 / Frac(3, 4), Frac(8, 3))

    def test_div_frac_float(self):
        self.assertEqual(Frac(2, 3) / 0.5, Frac(4, 3))

    def test_one_argument_operators(self):
        self.assertEqual(+Frac(1, 2), Frac(1, 2))
        self.assertEqual(+Frac(1, 2), Frac(-1, -2))
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(-Frac(1, 2), Frac(1, -2))
        self.assertEqual(~Frac(2, 3), Frac(3, 2))

    def test_float_frac(self):
        self.assertEqual(float(Frac(1, 2)), 1/2)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
