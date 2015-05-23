from django.db import models


class Day(models.Model):
    """
    Open hours for days of the week
    """
    # Constants for days of the week
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    # Choices to map day constants to Names
    day_choices = (
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday"),
    )

    day_name = models.IntegerField(choices=day_choices, unique=True, help_text="Name of the day of the week")
    start_time = models.CharField(blank=True, max_length=7, help_text="Time the shop opens")
    end_time = models.CharField(blank=True, max_length=7, help_text="Time the shop closes")

    def get_hours_range(self):
        """
        Get the hours to display for a given day - Either closed or a <start>-<end> format
        """
        if self.start_time == '' and self.end_time == '':
            return "Closed"
        # TODO Make this a real error case
        elif self.start_time == '' or self.end_time == '':
            return "Somethings Wrong"
        else:
            return self.start_time + "-" + self.end_time
