from time import mktime, time
from ciso8601 import parse_datetime
from datetime import datetime

def date_to_timestamp(date):
  """
  Convert date to timestamp

  :param date: date string '2019-04-30'
  :return: timestamp int 1546318800
  """
  ts = parse_datetime(date)
  # to get time in seconds:
  return int(mktime(ts.timetuple()))

def timestamp_to_date(timestamp):
  """
  Convert timestamp to readable date

  :param timestamp: timestamp string '1546318800'
  :return: date string '2019-04-30'
  """
  return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

def get_current_timestamp():
  return int(time())
