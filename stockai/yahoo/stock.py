from .base import Base
from ..utils import date_to_timestamp

class Stock(Base):
    def __init__(self, symbol):
        super(Stock, self).__init__(symbol)
        self.refresh()

    # Summary Profile
    def get_summary_profile(self):
        return self.data_set['summaryProfile']

    # Financial Data
    def get_price(self):
        return self.data_set['financialData']['currentPrice']['fmt']

    def get_currency(self):
        return self.data_set['financialData']['financialCurrency']

    # Historical Prices
    def get_historical_prices(self, start_date, end_date):
        if (date_to_timestamp(start_date) > date_to_timestamp(end_date)):
            raise ValueError('Please check the order of start date and end date')

        return self.get_historical(date_to_timestamp(start_date), date_to_timestamp(end_date))

    # Get all prices
    def get_all_prices(self):
      return self.get_all_historical()

