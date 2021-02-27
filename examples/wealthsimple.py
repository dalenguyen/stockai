import sys
sys.path.append('../stockai')

from stockai import WealthSimple

email: str = ''
password: str = ''

def prepare_credentails():
  global email, password
  print('Prepare credentials')
  while not email:
    email = str(input("Enter email: \n>>> "))
  while not password:
    password = str(input("Enter password: \n>>> "))

def init():
  global username, password

  ws = WealthSimple(email, password)

  print('Get me...\n')
  me = ws.get_me()
  print(me)

  print('Get accounts\n')
  accounts = ws.get_accounts()
  print(accounts)

  print('Get security \n')
  TSLA = ws.get_security('TSLA')
  print(TSLA)

prepare_credentails()
init()

