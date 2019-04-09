# Stock AI

[![PyPI version](https://badge.fury.io/py/stockai.svg)](https://badge.fury.io/py/stockai)
[![Build Status](https://travis-ci.org/dalenguyen/stockai.svg?branch=master)](https://travis-ci.org/dalenguyen/stockai)

Python module to get stock data from Yahoo! Finance

*This is an ongoing project. If you have any requests or contributions, please create a [ticket](https://github.com/dalenguyen/stockai/issues)*

## Install

From PyPI with pip

```sh
pip install stockai
```

## Usage examples

```python
from stockai import Stock
td = Stock('TD.TO')

print(td.get_summary_profile())
print(td.get_price())
print(td.get_currency())
```

## Get Historical Prices

```python
### The date format should be yyyy-mm-dd
td.get_historical_prices('2019-01-01', '2019-01-05')

### The result is a dictionary with ['volumn', 'low', 'open', 'hight', 'close', 'date', 'adjclose']
{  
   'volume':[  
      3930300,
      5407700,
      5103400
   ],
   'low':[  
      67.12000274658203,
      67.12000274658203,
      67.66999816894531
   ],
   'open':[  
      67.51000213623047,
      68.11000061035156,
      68.0
   ],
   'high':[  
      68.43000030517578,
      68.11000061035156,
      68.1500015258789
   ],
   'close':[  
      68.25,
      67.30000305175781,
      67.9800033569336
   ],
   'date':[  
      '2019-01-02',
      '2019-01-03',
      '2019-01-04'
   ],
   'adjclose':[  
      67.57575225830078,
      66.63513946533203,
      67.30841827392578
   ]
}
```