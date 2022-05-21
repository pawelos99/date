from unittest import TestCase

from date import Date


class TestDate(TestCase):
    def test_create_simple_date(self) -> None:
        d = Date.from_string("21.05.2020")
        self.assertEqual(d.year, 2020)
        self.assertEqual(d.month, 5)
        self.assertEqual(d.day, 21)

    def test_create_wrong_date(self) -> None:
        examples = [
            "0.12.12",
            "21.0.12",
            "29.02.2019",
            "30.02.2020",
            "32.12.2021",
            "1.13.1",
        ]
        for example in examples:
            with self.assertRaises(ValueError):
                Date.from_string(example)

    def test_create_date_leap_year(self) -> None:
        d = Date.from_string("29.02.2020")
        self.assertEqual(d.day, 29)

    def test_leap_year(self) -> None:
        for year in [2000, 2004]:
            self.assertTrue(Date.is_year_leap(year=year))

    def test_not_a_leap_year(self) -> None:
        for year in [1900, 2003]:
            self.assertFalse(Date.is_year_leap(year=year))

    def test_get_day_of_year(self) -> None:
        data = [
            ("01.01.2020", 1),
            ("31.12.2019", 365),
            ("31.12.2020", 366),
            ("01.03.2020", 61),
        ]
        for date, day_of_the_year in data:
            self.assertEqual(
                Date.from_string(text=date).day_of_the_year, day_of_the_year
            )

    def test_add_days_the_same_month(self) -> None:
        d = Date(day=10, month=5, year=2020)
        d.add_days(number_of_days=20)
        self.assertEqual(d.day, 30)
        self.assertEqual(d.month, 5)
        self.assertEqual(d.year, 2020)

    def test_add_zero_days(self) -> None:
        d = Date(day=10, month=5, year=2020)
        d.add_days(number_of_days=0)
        self.assertEqual(d.day, 10)
        self.assertEqual(d.month, 5)
        self.assertEqual(d.year, 2020)

    def test_add_days_next_month(self) -> None:
        values = [
            (22, Date(day=1, month=2, year=2020)),
            (50, Date(day=29, month=2, year=2020)),
            (356, Date(day=31, month=12, year=2020)),
        ]
        for value, expected_day in values:
            d = Date(day=10, month=1, year=2020)
            d.add_days(number_of_days=value)
            self.assertEqual(d, expected_day)

    def test_add_days_next_year(self) -> None:
        # confirmed by running:
        # >>> datetime.datetime(day=10, month=1, year=2020) + datetime.timedelta(days=1000000)
        # datetime.datetime(4757, 12, 7, 0, 0)
        values = [
            (357, Date(day=1, month=1, year=2021)),
            (1000000, Date(day=7, month=12, year=4757)),
        ]
        for value, expected_day in values:
            d = Date(day=10, month=1, year=2020)
            d.add_days(number_of_days=value)
            self.assertEqual(d, expected_day)
