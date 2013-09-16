from outils.dateutils import convert_to_list_month
from django.test import TestCase
import datetime


class DateutilsTest(TestCase):
    def test_convert_to_list_month(self):
        """
        Test function to render a list of months
        """
        start_date = datetime.date(year=2013, month=9, day=3)
        stop_date = datetime.date(year=2014, month=2, day=5)
        # solution = [('1', 'September'),('2', 'October')('3', 'November'),('4', 'December')('5', 'January'),('6', 'February')]
        answer = convert_to_list_month(start_date, stop_date)
        self.assertEqual(solution, 'd')
