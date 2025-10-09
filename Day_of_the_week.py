from datetime import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date_obj = datetime(year, month, day)
        day_of_week = date_obj.strftime("%A")

        print("Day of the week:", day_of_week)

        return day_of_week

# optimal solutoin very easy 