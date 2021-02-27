from requests import Session
from .requests import WSAPIRequest
from loguru import logger

class WealthSimple():
  BASE_DOMAIN = 'https://trade-service.wealthsimple.com/'

  def __init__(self, email: str, password: str):
    self.session = Session()
    self.WSAPI = WSAPIRequest(self.session, self.BASE_DOMAIN)
    self.login(email, password)

  def login (self, email: str = None, password: str = None) -> None:
    if email and password:
      payload = { "email": email, "password": password, "timeoutMs": 2e4 }
      response = self.WSAPI.request('POST', 'auth/login', payload)

      # Check of OTP
      if "x-wealthsimple-otp" in response.headers:
        TFACode = ''
        while not TFACode:
            # Obtain user input and ensure it is not empty
            TFACode = input('Enter 2FA code: ')
        payload['otp'] =  TFACode
        response = self.WSAPI.request('POST', 'auth/login', payload)

      if response.status_code == 401:
        raise Exception('Invalid Login')

      self.session.headers.update(
              {"Authorization": response.headers["X-Access-Token"]}
          )
      self.session.headers.update(
              {"refresh_token": response.headers["X-Refresh-Token"]}
          )
    else:
      raise Exception('Missing login credentials')

  def get_me(self):
    logger.debug('get_me')
    response = self.WSAPI.request('GET', 'me')
    logger.debug(f'get_me {response.status_code}')

    if response.status_code == 401:
      raise Exception('Invalid Access Token')
    else:
      return response.json()

  def get_accounts(self) -> list:
    """
    Get Wealthsimple Trade Accounts
    """
    response = self.WSAPI.request('GET', 'account/list')
    response = response.json()
    return response['results']

  def get_security(self, id: str) -> dict:
      """
      Get Security Info
      """
      logger.debug('get_security')
      response = self.WSAPI.request('GET', f'securities/{id}')
      logger.debug(f"get_security {response.status_code}")

      if response.status_code == 401:
            raise Exception(f'Cannot get security {id}')
      else:
          return response.json()
