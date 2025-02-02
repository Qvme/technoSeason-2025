import unittest
from src.date_calculator import DateCalculator, DateException

class TestDateCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = DateCalculator()

    def test_is_leap_year(self):
        self.assertTrue(DateCalculator.is_leap(2000))
        self.assertTrue(DateCalculator.is_leap(2004))
        self.assertFalse(DateCalculator.is_leap(2100))
        self.assertFalse(DateCalculator.is_leap(2023))

    def test_is_valid_date(self):
        self.assertTrue(DateCalculator.is_valid_date("1-1-2000"))
        self.assertTrue(DateCalculator.is_valid_date("31-12-2023"))
        self.assertFalse(DateCalculator.is_valid_date("31-4-2023"))  # April has 30 days
        self.assertFalse(DateCalculator.is_valid_date("29-2-2023"))  # Not a leap year

    def test_predict_day(self):
        # Test cases for predict_day
        test_cases = [
            ("1-1-2000", "sat"),  # Reference date
            ("2-1-2000", "sun"),
            ("31-12-1999", "fri"),
            ("1-1-2024", "mon")
        ]
        
        for date, expected in test_cases:
            with self.subTest(date=date):
                self.assertEqual(self.calculator.predict_day(date), expected)

    def test_invalid_date_exception(self):
        with self.assertRaises(DateException):
            DateCalculator("32-1-2000")  # Invalid reference date
        
        with self.assertRaises(DateException):
            self.calculator.predict_day("29-2-2023")  # Invalid input date

if __name__ == '__main__':
    unittest.main() 