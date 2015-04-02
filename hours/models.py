from django.db import models


class Day(models.Model):
    """
    Open hours for days of the week
    """
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

    dayName = models.IntegerField(choices=dayChoices, unique=True, help_text="Name of the day of the week")
    startTime = models.CharField(blank=True, max_length=5, help_text="Time the shop opens")
    endTime = models.CharField(blank=True, max_length=5, help_text="Time the shop closes")

    def getHoursRange(self):
        """
        Get the hours to display for a given day - Either closed or a <start>-<end> format
        """
        if self.startTime=='' and self.endTime=='':
            return "Closed"
        #Make this a real error case
        elif self.startTime=='' or self.endTime =='':
            return "Somethings Wrong"
        else:
            return self.startTime + "-" + self.endTime
