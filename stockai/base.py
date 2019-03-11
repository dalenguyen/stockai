from requests import get

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

    def refresh(self):
        """
        Refresh stock data
        """
        self.data_set = self._request()