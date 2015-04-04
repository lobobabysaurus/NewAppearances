from django.test import TestCase

from hours.models import Day

class HourStringTest(TestCase):
    """
    Tests for the formatting of the open hours display
    """
    def testClosed(self):
        """
        Test that a day with no specified hours appears as closed
        """
        closedDay = Day(dayName=Day.MONDAY)
        self.assertEquals(closedDay.getHoursRange(), "Closed", "Output when closed is not as expected")
    def testOpen(self):
        """
        Tests that a day with specified hours appears as expected
        """
        openDay = Day(dayName=Day.TUESDAY, startTime="6:00", endTime="10:00")
        self.assertEquals(openDay.getHoursRange(), "6:00-10:00", "Time range is not displaying as expected")