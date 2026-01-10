"""
Tutorial 2, Question 1.

Print leap years within a given range (1900 to 2020).
"""


class LeapYear:
    """Calculates leap years."""

    def __init__(self, start_year, end_year):
        if not (isinstance(start_year, int) and isinstance(end_year, int)):
            raise TypeError("Invalid Year Input.")
        
        if end_year < start_year:
            raise ValueError("Start Year must preceed End Year.")

        self.start_year = start_year
        self.end_year = end_year
        self.leap_years = []


    def get_leap_year(self):
        """Reiterates through each year"""

        years_list = list(range(self.start_year, self.end_year))

        for year in years_list:
            if year%4 == 0 and (year%100 != 0 or year%400 == 0):
                self.leap_years.append(year)
        
        return 0


if __name__ == "__main__":
    check_years = LeapYear(1900,2020)
    check_years.get_leap_year()
    if len(check_years.leap_years) == 0:
        print(f"There are no leap years between {check_years.start_year} and {check_years.end_year}.")
    else:
        print(
            f"Between the years {check_years.start_year} and {check_years.end_year}, "
            f"the leap years are: "
        )
    for year in check_years.leap_years:
        print(year)
    
