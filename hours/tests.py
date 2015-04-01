from django.test import TestCase

from hours.models import Day

class HourStringTest(TestCase):
    def testClosed(self):
        closedDay = Day(dayName=Day.MONDAY)
        self.assertEquals(closedDay.getHoursRange(), "Closed", "Output when closed is not as expected")
    def testOpen(self):
        openDay = Day(dayName=Day.TUESDAY, startTime="6:00", endTime="10:00")
        self.assertEquals(openDay.getHoursRange(), "6:00-10:00", "Time range is not displaying as expected")