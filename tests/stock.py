import sys
sys.path.append('../stockai')

if sys.version_info < (2, 7):
    from unittest2 import main as test_main, SkipTest, TestCase
else:
    from unittest import main as test_main, SkipTest, TestCase

from stockai import Stock

class TestStock(TestCase):

    def setUp(self):
        self.td = Stock('TD.TO')

    def test_td_summary_profile(self):
        self.assertEqual(self.td.get_summary_profile()['city'], 'Toronto')

    def test_td_financial_data(self):
        float(self.td.get_price())
        self.assertEqual(self.td.get_currency(), 'CAD')

    def test_td_historical_prices(self):
        dict(self.td.get_historical_prices('2019-01-01', '2019-01-05'))

if __name__ == "__main__":
    test_main()
