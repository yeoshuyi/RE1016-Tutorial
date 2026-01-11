"""
Tutorial 3, Question 3.

Program that parses input in the form:
MM/DD/YYYY HR:MIN:SEC
And prints reformatted information.
Data validation done for the following:
1) Correct spacers '/', ' ', ':'.
2) Total string length.
3) All data is integer.
4) All data makes sense (Including leap year logic).
"""


class StoreDateTime:
    """Stores datetime based on input"""

    def __init__(self, string):
        if not isinstance(string, str):
            raise TypeError("Wrong input type.")
        if (string[2] != '/'
            or string[5] != '/'
            or string[10] != ' '
            or string[13] != ':' 
            or string[16] != ':' 
            or len(string) != 19):
            raise ValueError("Wrong input format.")
        try:
            day = int(string[0:2])
            month = int(string[3:5])
            year = int(string[6:10])
            hour = int(string[11:13])
            min = int(string[14:16])
            second = int(string[17:19])
        except ValueError:
            raise ValueError("Wrong input format.")
        
        if 0 <= year:
            self.year = year
        else:
            raise ValueError("Year must be realistic.")
        
        if 1 <= month <= 12:
            self.month = month
        else:
            raise ValueError("Month must be realistic.")
        
        if month == 2:
            # Leap year logic from previous tutorial
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day_limit = 29
            else:
                day_limit = 28
        elif month in [4, 6, 9, 11]:
            day_limit = 30
        else:
            day_limit = 31
        if 1 <= day <= day_limit:
            self.day = day
        else:
            raise ValueError("Day must be realistic.")
        
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            raise ValueError("Hour must be realistic.")
        
        if 0 <= min <= 59:
            self.min = min
        else:
            raise ValueError("Minute must be realistic.")
        
        if 0 <= second <= 59:
            self.second = second
        else:
            raise ValueError("Second must be realistic.")

    def print_info(self):
        """Prints information on the stored datetime"""

        print(
            f"Date Time Stored:\n"
            f"{self.day:02d}/{self.month:02d}/{self.year:04d}\n"
            f"{self.hour:02d}:{self.min:02d}:{self.second:02d}\n"
            f"The time now is in "
            ,end=''
        )
        if self.hour > 11:
            print("PM.")
        else:
            print("AM.")
        return 0 

if __name__ == "__main__":
    test_string = StoreDateTime("28/02/4567 23:01:23")
    test_string.print_info()