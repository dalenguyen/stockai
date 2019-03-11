# Stock AI

Python module to get stock data from Yahoo! Finance

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