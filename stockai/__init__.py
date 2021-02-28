"""
Stockai - get stock information from Yahoo! Finance
"""

__version__ = '1.5.0'
__author__ = 'Dale Nguyen'
__name__ = 'stockai'

from .yahoo.stock import Stock
from .wealthsimple.stock import WealthSimple
