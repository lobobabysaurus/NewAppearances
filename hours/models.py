from django.db import models
"""
Model for represent open hours for days of the week
"""
class Day(models.Model):
    # Constants for days of the week
    MONDAY=1
    TUESDAY=2
    WEDNESDAY=3
    THURSDAY=4
    FRIDAY=5
    SATURDAY=6
    SUNDAY=7

    # Choices to map day constants to Names
    dayChoices = (
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday"),
    )

    # Name of the day of the week
    dayName = models.IntegerField(choices=dayChoices,unique=True,)
    # Start and End times for the shop for that day
    startTime = models.CharField(blank=True, max_length=5,)
    endTime = models.CharField(blank=True, max_length=5,)

    """
    Get the hours display for a given day
    :return a string showing the range of hours for a day or Closed if the salon is not open
    """
    def getHoursRange(self):
        if (self.startTime=='' and self.endTime==''):
            return "Closed"
        #Make this a real error case
        elif(self.startTime=='' or self.endTime ==''):
            return "Somethings Wrong"
        else:
            return self.startTime + "-" + self.endTime
