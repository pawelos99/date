class Date:
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day: int, month: int, year: int) -> None:
        self.year = self._validate_year(year=year)
        self.month = self._validate_month(month)
        self.day = self._validate_day(day)

    @staticmethod
    def is_year_leap(year: int) -> bool:
        if not year % 400:
            return True
        if not year % 100:
            return False
        if not year % 4:
            return True
        return False

    @property
    def day_of_the_year(self) -> int:
        sum_of_days = sum(self.DAYS_IN_MONTH[: self.month - 1]) + self.day
        if not self.is_year_leap(year=self.year) or self.month <= 2:
            return sum_of_days
        return sum_of_days + 1

    @classmethod
    def from_string(cls, text: str) -> "Date":
        day, month, year = text.split(".")
        return cls(day=day, month=month, year=year)

    @staticmethod
    def _validate_year(year: int) -> int:
        try:
            return int(year)
        except ValueError:
            raise ValueError(f"Year {year} must be a int like value")

    @staticmethod
    def _validate_month(month: int) -> int:
        try:
            month = int(month)
        except ValueError:
            raise ValueError(f"Month {month} must be a int like value")
        if month < 1 or month > 12:
            raise ValueError(f"Wrong number of months: {month}")
        return month

    @classmethod
    def get_days_in_month(cls, month: int, year: int) -> int:
        days_in_month = cls.DAYS_IN_MONTH[month - 1]
        if month == 2 and cls.is_year_leap(year=year):
            days_in_month += 1
        return days_in_month

    def _validate_day(self, day: int) -> int:
        try:
            day = int(day)
        except ValueError:
            raise ValueError(f"Day {day} must be a int like value")
        days_in_month = self.get_days_in_month(month=self.month, year=self.year)
        if day < 1 or day > days_in_month:
            raise ValueError("Wrong number of days")
        return day

    def add_days(self, number_of_days: int) -> None:
        try:
            number_of_days = int(number_of_days)
        except ValueError:
            raise ValueError(f"Number of days is not a number: {number_of_days}")
        if number_of_days < 0:
            raise ValueError("Number of days to add must be positive")
        while True:
            days_in_month = self.get_days_in_month(month=self.month, year=self.year)
            if number_of_days + self.day <= days_in_month:
                self.day += number_of_days
                return
            number_of_days -= days_in_month - self.day + 1
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def __repr__(self) -> str:
        return f"Date: {self.year}.{self.month}.{self.day}"

    def __eq__(self, other: "Date") -> bool:
        return all(
            [self.year == other.year, self.day, other.day, self.month == other.month]
        )
