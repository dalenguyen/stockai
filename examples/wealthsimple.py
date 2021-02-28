from loguru import logger
from stockai import WealthSimple
import sys
sys.path.append('../stockai')

email: str = ''
password: str = ''


def prepare_credentails():
    global email, password

    logger.debug('Prepare credentials')

    while not email:
        email = str(input("Enter email: \n>>> "))
    while not password:
        password = str(input("Enter password: \n>>> "))


def init():
    global username, password

    ws = WealthSimple(email, password)

    logger.debug('Get me...')
    me = ws.get_me()
    print(me)

    logger.debug('Get accounts')
    accounts = ws.get_accounts()
    print(accounts)

    logger.debug('Refresh tokens\n)
    ws.refresh_tokens()

    print(ws.session.headers['Authorization'])

    logger.debug('Get security')
    TSLA = ws.get_security('TSLA')
    print(TSLA)


prepare_credentails()
init()
