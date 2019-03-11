"""
Yahoo.py: Yahoo search results with python
Usage: print search("what does the fox say?")
"""
version__ = '0.0.1'
author__ = 'Dale Nguyen'
name = 'stockai'

# https://query2.finance.yahoo.com/v1/finance/quoteType/TD.TO?lang=en-US&region=US&corsDomain=finance.yahoo.com
# 
from requests import get

def search():
    r = get('https://query2.finance.yahoo.com/v10/finance/quoteSummary/TD.TO?formatted=true&crumb=jf%2FC73R5qYx&lang=en-US&region=US&modules=price%2CsummaryDetail%2CpageViews&corsDomain=finance.yahoo.com')
    print(r.status_code)
    print(r.json())

class Base(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def _prepare_request(self, region='US', lang='en-US', includePrePost='false', interval='2m', range='1d'):
        """
        Basic Yahoo Rquest URL
        """

        url = 'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?region={region}&lang={lang}&includePrePost={includePrePost}&interval={interval}&range={range}&corsDomain=finance.yahoo.com&.tsrc=finance'.format(
            symbol = self.symbol,
            region = region,
            lang = lang,
            includePrePost = includePrePost,
            interval = interval,
            range = range
        )

        print(url)

        return url

    def _request(self):
        url = self._prepare_request()
        data = get(url)
        return data.json()

class Stock(Base):
    def __init__(self, symbol):
        super(Stock, self).__init__(symbol)
        print(self._request())


test = Stock('TD.TO')
print(test)