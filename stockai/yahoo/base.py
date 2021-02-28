from requests import get
from ..utils import timestamp_to_date, get_current_timestamp

class Base(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def __prepare_request(self, region='US', lang='en-US', includePrePost='false', interval='2m', range='1d'):
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

    def __request(self):
        url = self.__prepare_request()
        data = get(url)

        if data.json()['quoteSummary']['error'] is not None:
            raise NameError(data.json()['quoteSummary']['error']['description'])

        return data.json()['quoteSummary']['result'][0]

    def get_historical(self, start_date, end_date, interval):
        interval = self.__get_interval(interval)

        url = 'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?formatted=true&period1={start_date}&period2={end_date}&interval={interval}&events=div%7Csplit&corsDomain=finance.yahoo.com'.format(
            symbol = self.symbol,
            start_date = start_date,
            end_date = end_date,
            interval = interval
        )
        data = get(url)
        return self.__process_historical_result(data)

    def get_all_historical(self, interval):
      # Start from 01/01/2000
      start_date = 946702800
      end_date = get_current_timestamp()
      return self.get_historical(start_date, end_date, interval)

    def refresh(self):
        """
        Refresh stock data
        """
        self.data_set = self.__request()

    def __process_historical_result(self, data):
      """
      Process data from Yahoo
      """
      if data.json()['chart']['error'] is not None:
          raise NameError(data.json()['chart']['error']['description'])

      result = data.json()['chart']['result'][0]['indicators']['quote'][0]
      date_data = { 'date' : data.json()['chart']['result'][0]['timestamp']}
      result['adjclose'] = data.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
      # result['meta'] = data.json()['chart']['result'][0]['meta']

      # for index, date in enumerate(result['date']):
      #     result['date'][index] = timestamp_to_date(result['date'][index])

      return {**date_data, **result}

    def __get_interval(self, interval):
      """Return interval value before sending requests

      Parameters
      ----------
      interval: 'daily' | 'weekly' | 'monthly'

      Returns
      ----------
      '1d' | '1wk' | '1mo'
      """
      return {
        'daily': '1d',
        'weekly': '1wk',
        'monthly': '1mo'
      }[interval]
