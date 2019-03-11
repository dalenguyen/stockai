from .base import Base

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

