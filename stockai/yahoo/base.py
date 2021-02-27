from requests import get
from ..utils import timestamp_to_date

class Base(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def _prepare_request(self, region='US', lang='en-US', includePrePost='false', interval='2m', range='1d'):
        """
        Basic Yahoo Rquest URL
        """
        url = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?formatted=true&lang={lang}&region=CA&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents%2CesgScores%2Cdetails%2Cprice&corsDomain=ca.finance.yahoo.com'.format(
            symbol = self.symbol,
            region = region,
            lang = lang,
            includePrePost = includePrePost,
            interval = interval,
            range = range
        )        

        return url

    def _request(self):
        url = self._prepare_request()
        data = get(url)
        
        if data.json()['quoteSummary']['error'] is not None:
            raise NameError(data.json()['quoteSummary']['error']['description'])
        
        return data.json()['quoteSummary']['result'][0]

    def get_historical(self, start_date, end_date):
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?formatted=true&period1={start_date}&period2={end_date}&interval=1d&events=div%7Csplit&corsDomain=finance.yahoo.com'.format(
            symbol = self.symbol,
            start_date = start_date,
            end_date = end_date
        )
        data = get(url)

        if data.json()['chart']['error'] is not None:
            raise NameError(data.json()['chart']['error']['description'])

        result = data.json()['chart']['result'][0]['indicators']['quote'][0]
        result['date'] = data.json()['chart']['result'][0]['timestamp']
        result['adjclose'] = data.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

        for index, date in enumerate(result['date']):
            result['date'][index] = timestamp_to_date(result['date'][index])
        
        return result

    def refresh(self):
        """
        Refresh stock data
        """
        self.data_set = self._request()