from django.test import TestCase

from .models import Day


class HourStringTest(TestCase):
    """
    Tests for the formatting of the open hours display
    """
    def testClosed(self):
        """
        Test that a day with no specified hours appears as closed
        """
        closed_day = Day(day_name=Day.MONDAY)
        self.assertEquals(closed_day.get_hours_range(), "Closed", "Output when closed is not as expected")

    def testOpen(self):
        """
        Tests that a day with specified hours appears as expected
        """
        open_day = Day(day_name=Day.TUESDAY, start_time="6:00", end_time="10:00")
        self.assertEquals(open_day.get_hours_range(), "6:00-10:00", "Time range is not displaying as expected")
