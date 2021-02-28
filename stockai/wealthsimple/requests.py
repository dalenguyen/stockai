import requests


class WSAPIRequest:
    """
    Handle API requests for WealthSimple
    """

    def __init__(self, session, ws_url):
        self.session = session
        self.WS_URL = ws_url

    def request(self, method, endpoint, params=None):
        url = self.WS_URL + endpoint

        if method == 'POST':
            return self.__post(url, params)
        elif method == 'GET':
            return self.__get(url, params)
        else:
            raise Exception('Invalid request method: {method}')

    def __post(self, url, params=None):
        try:
            return self.session.post(url, params)
        except Exception as error:
            print(error)

    def __get(self, url, payload=None):
        auth = self.session.headers['Authorization']
        return requests.get(url,  headers={'Authorization': auth})
