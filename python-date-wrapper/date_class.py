from datetime import date, timedelta
import calendar

class Date:
    def __init__(self, month=1, day=1, year=1900):
        self.__date = date(year, month, day)
          
    @property
    def month(self) -> int:
        return self.__date.month
      
    @property   
    def day(self) -> int:
        return self.__date.day
        
    @property
    def year(self) -> int:
        return self.__date.year
        

    def set_date(self, month: int, day: int, year: int) -> None:
        new_date = date(year, month, day)
        self.__date = new_date

    def is_leap_year(self) -> bool:
        return calendar.isleap(self.__date.year)

    def __sub__(self, other: object) -> int:
        """Return the signed number of days between two Date objects."""
        if not isinstance(other, Date):
            return NotImplemented

        difference = self.__date - other.__date
        return difference.days

    def increment(self) -> "Date":
        """Increase this date by one day and return the same object."""
        self.__date += timedelta(days=1)
        return self

    def decrement(self) -> "Date":
        """Decrease this date by one day and return the same object."""
        self.__date -= timedelta(days=1)
        return self

    def __str__(self) -> str:
        """Return the date in Month Day, Year format."""
        return self.__date.strftime("%B %d, %Y").replace(" 0", " ")

    @classmethod
    def from_input(cls) -> "Date":
        """Prompt for a date and return a new Date. Invalid input raises ValueError."""
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        year = int(input("Enter year: "))

        return cls(month, day, year)