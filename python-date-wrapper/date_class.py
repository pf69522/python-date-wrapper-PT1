from datetime import date
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

