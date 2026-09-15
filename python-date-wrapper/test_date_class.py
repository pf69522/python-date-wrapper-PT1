import unittest
from date_class import Date

class TestDate(unittest.TestCase):
    def test_default_constructor(self):
       d = Date()
       self.assertEqual(d.month, 1)
       self.assertEqual(d.day, 1)
       self.assertEqual(d.year, 1900)

   
    def test_valid_constructor(self):
        d = Date(12, 25, 2021)
        self.assertEqual(d.month, 12)
        self.assertEqual(d.day, 25)
        self.assertEqual(d.year, 2021)

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            Date(13, 1, 2025)

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            Date(4, 32, 2025)

    def test_invalid_leap_day(self):
        with self.assertRaises(ValueError):
            Date(2, 29, 2025)

    def test_set_date(self):
        d = Date()

        d.set_date(12, 25, 2025)

        self.assertEqual(d.month, 12)
        self.assertEqual(d.day, 25)
        self.assertEqual(d.year, 2025)
