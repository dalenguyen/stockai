from .base import Base
from ..utils import date_to_timestamp

class Stock(Base):
    def __init__(self, symbol):
        super(Stock, self).__init__(symbol)
        self.refresh()

    def get_summary_profile(self):
      """Return summary profile of a security"""
      return self.data_set['summaryProfile']

    def get_info(self):
      """Return detail information of a security"""
      return self.data_set['price']

    def get_price(self):
      """Return price of a security"""
      return self.data_set['financialData']['currentPrice']['fmt']

    def get_currency(self):
      """Return currency of a security"""
      return self.data_set['financialData']['financialCurrency']

    def get_historical_prices(self, start_date, end_date):
      """Return historical prices of a security
      Parameters
      ----------
      start_date: str
        Start date
      end_date: str
        End date
      """
      if (date_to_timestamp(start_date) > date_to_timestamp(end_date)):
          raise ValueError('Please check the order of start date and end date')

      return self.get_historical(date_to_timestamp(start_date), date_to_timestamp(end_date))

    def get_all_prices(self):
      """Return all historical prices starting from 01/01/2000"""
      return self.get_all_historical()

