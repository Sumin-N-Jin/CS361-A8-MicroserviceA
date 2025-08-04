import unittest
from converter import convert_utc_to_local

class TestConverter(unittest.TestCase):
    def test_normal(self):
        result = convert_utc_to_local("2025-08-01 13:00", -8, False)
        self.assertEqual(result["date"], "2025-08-01")
        self.assertEqual(result["time"], "05:00")

    def test_dst(self):
        result = convert_utc_to_local("2025-08-01 13:00", -8, True)
        self.assertEqual(result["date"], "2025-08-01")
        self.assertEqual(result["time"], "06:00")

    def test_positive_offset(self):
        result = convert_utc_to_local("2025-08-01 13:00", 9, False)
        self.assertEqual(result["date"], "2025-08-01")
        self.assertEqual(result["time"], "22:00")

    def test_day_rollover(self):
        result = convert_utc_to_local("2025-08-01 01:00", -3, False)
        self.assertEqual(result["date"], "2025-07-31")
        self.assertEqual(result["time"], "22:00")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_utc_to_local("2025/08/01", -8, False)


if __name__ == "__main__":
    unittest.main()