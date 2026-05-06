import unittest

from mesfonctions import (
    compter_voyelles,
    division,
    est_pair,
    factorielle,
    maximum_liste,
)


class TestMesFonctions(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        with self.assertRaises(ValueError):
            division(10, 0)

    def test_est_pair(self):
        self.assertTrue(est_pair(8))
        self.assertFalse(est_pair(7))

    def test_factorielle(self):
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(5), 120)
        with self.assertRaises(ValueError):
            factorielle(-1)

    def test_compter_voyelles(self):
        self.assertEqual(compter_voyelles("Bonjour"), 3)
        self.assertEqual(compter_voyelles("XYZ"), 1)

    def test_maximum_liste(self):
        self.assertEqual(maximum_liste([4, 9, 2, 7]), 9)
        with self.assertRaises(ValueError):
            maximum_liste([])


if __name__ == "__main__":
    unittest.main()
