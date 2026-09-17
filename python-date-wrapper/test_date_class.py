import unittest
from date_class import Date
from unittest.mock import patch

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

    def test_leap_year(self):
        d = Date(2, 29, 2024)
        
        self.assertTrue(d.is_leap_year())


    def test_positive_subtraction(self):
        first_date = Date(4, 18, 2014)
        second_date = Date(4, 10, 2014)

        self.assertEqual(first_date - second_date, 8)

    def test_negative_subtraction(self):
        first_date = Date(4, 10, 2014)
        second_date = Date(4, 18, 2014)

        self.assertEqual(first_date - second_date, -8)

    def test_equal_date_subtraction(self):
        first_date = Date(4, 18, 2014)
        second_date = Date(4, 18, 2014)

        self.assertEqual(first_date - second_date, 0)

    def test_different_month_subtraction(self):
        first_date = Date(5, 10, 2014)
        second_date = Date(4, 10, 2014)

        self.assertEqual(first_date - second_date, 30)

    def test_different_year_subtraction(self):
        first_date = Date(1, 1, 2025)
        second_date = Date(1, 1, 2024)

        self.assertEqual(first_date - second_date, 366)

    def test_subtraction_across_leap_day(self):
        first_date = Date(3, 1, 2024)
        second_date = Date(2, 28, 2024)

        self.assertEqual(first_date - second_date, 2)

    def test_long_range_subtraction(self):
        first_date = Date(2, 2, 2006)
        second_date = Date(11, 10, 2003)

        self.assertEqual(first_date - second_date, 815)

    def test_unsupported_subtraction(self):
        test_date = Date(4, 18, 2014)

        with self.assertRaises(TypeError):
            test_date - 5

    def test_normal_increment(self):
        test_date = Date(4, 18, 2018)

        test_date.increment()

        self.assertEqual(test_date.month, 4)
        self.assertEqual(test_date.day, 19)
        self.assertEqual(test_date.year, 2018)

    def test_increment_april_to_may(self):
        test_date = Date(4, 30, 2018)

        test_date.increment()

        self.assertEqual(test_date.month, 5)
        self.assertEqual(test_date.day, 1)
        self.assertEqual(test_date.year, 2018)

    def test_increment_january_to_february(self):
        test_date = Date(1, 31, 2018)

        test_date.increment()

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 1)
        self.assertEqual(test_date.year, 2018)

    def test_increment_non_leap_year(self):
        test_date = Date(2, 28, 2025)

        test_date.increment()

        self.assertEqual(test_date.month, 3)
        self.assertEqual(test_date.day, 1)
        self.assertEqual(test_date.year, 2025)

    def test_increment_to_leap_day(self):
        test_date = Date(2, 28, 2024)

        test_date.increment()

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 29)
        self.assertEqual(test_date.year, 2024)

    def test_increment_after_leap_day(self):
        test_date = Date(2, 29, 2024)

        test_date.increment()

        self.assertEqual(test_date.month, 3)
        self.assertEqual(test_date.day, 1)
        self.assertEqual(test_date.year, 2024)

    def test_increment_year_boundary(self):
        test_date = Date(12, 31, 2024)

        test_date.increment()

        self.assertEqual(test_date.month, 1)
        self.assertEqual(test_date.day, 1)
        self.assertEqual(test_date.year, 2025)

    def test_increment_returns_same_object(self):
        test_date = Date(4, 18, 2018)

        returned_value = test_date.increment()

        self.assertIs(returned_value, test_date)

    def test_normal_decrement(self):
        test_date = Date(4, 18, 2018)

        test_date.decrement()

        self.assertEqual(test_date.month, 4)
        self.assertEqual(test_date.day, 17)
        self.assertEqual(test_date.year, 2018)

    def test_decrement_may_to_april(self):
        test_date = Date(5, 1, 2018)

        test_date.decrement()

        self.assertEqual(test_date.month, 4)
        self.assertEqual(test_date.day, 30)
        self.assertEqual(test_date.year, 2018)

    def test_decrement_non_leap_year(self):
        test_date = Date(3, 1, 2025)
        test_date.decrement()

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 28)
        self.assertEqual(test_date.year, 2025)

    def test_decrement_leap_year(self):
        test_date = Date(3, 1, 2024)
        test_date.decrement()

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 29)
        self.assertEqual(test_date.year, 2024)

    def test_decrement_year_boundary(self):
        test_date = Date(1, 1, 2025)
        test_date.decrement()

        self.assertEqual(test_date.month, 12)
        self.assertEqual(test_date.day, 31)
        self.assertEqual(test_date.year, 2024)

    def test_decrement_returns_same_object(self):
        test_date = Date(4, 18, 2018)

        returned_value = test_date.decrement()

        self.assertIs(returned_value, test_date)

    def test_decrement_non_leap_year(self):
        test_date = Date(3, 1, 2025)
        test_date.decrement()

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 28)
        self.assertEqual(test_date.year, 2025)

    def test_decrement_leap_year(self):
        test_date = Date(3, 1, 2024)
        test_date.decrement()

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 29)
        self.assertEqual(test_date.year, 2024)

    def test_decrement_year_boundary(self):
        test_date = Date(1, 1, 2025)
        test_date.decrement()

        self.assertEqual(test_date.month, 12)
        self.assertEqual(test_date.day, 31)
        self.assertEqual(test_date.year, 2024)

    def test_decrement_returns_same_object(self):
        test_date = Date(4, 18, 2018)

        returned_value = test_date.decrement()

        self.assertIs(returned_value, test_date)

    def test_string_output(self):
        test_date = Date(4, 18, 2018)
        self.assertEqual(str(test_date), "April 18, 2018")

    def test_string_single_digit_day(self):
        test_date = Date(4, 8, 2018)
        self.assertEqual(str(test_date), "April 8, 2018")

    def test_string_leap_day(self):
        test_date = Date(2, 29, 2024)
        self.assertEqual(str(test_date), "February 29, 2024")

    def test_string_year_boundary(self):
        test_date = Date(12, 31, 2024)
        self.assertEqual(str(test_date), "December 31, 2024")

    @patch("builtins.input", side_effect=["4", "18", "2018"])
    def test_from_input_valid(self, mock_input):
        result = Date.from_input()

        self.assertEqual(result.month, 4)
        self.assertEqual(result.day, 18)
        self.assertEqual(result.year, 2018)

    @patch("builtins.input", side_effect=["hello", "18", "2018"])
    def test_from_input_nonnumeric(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["13", "18", "2018"])
    def test_from_input_invalid_month(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["4", "32", "2018"])
    def test_from_input_invalid_day(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["2", "29", "2025"])
    def test_from_input_invalid_leap_day(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()