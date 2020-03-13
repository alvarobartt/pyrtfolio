# pyrtfolio - Python package to generate stock portfolios

[![Python Version](https://img.shields.io/pypi/pyversions/pyrtfolio.svg)](https://pypi.org/project/pyrtfolio/)
[![PyPi Version](https://img.shields.io/pypi/v/pyrtfolio.svg)](https://pypi.org/project/pyrtfolio/)
[![Package Status](https://img.shields.io/pypi/status/pyrtfolio.svg)](https://pypi.org/project/pyrtfolio/)
[![Build Status](https://dev.azure.com/alvarob96/alvarob96/_apis/build/status/alvarob96.pyrtfolio?branchName=master)](https://dev.azure.com/alvarob96/alvarob96/_build?definitionId=1&_a=summary)
[![Build Status](https://img.shields.io/travis/alvarob96/pyrtfolio/master.svg?label=Travis%20CI&logo=travis&logoColor=white)](https://travis-ci.org/alvarob96/pyrtfolio)
[![Documentation Status](https://readthedocs.org/projects/pyrtfolio/badge/?version=latest)](https://pyrtfolio.readthedocs.io/)
[![codecov](https://codecov.io/gh/alvarob96/pyrtfolio/branch/master/graph/badge.svg)](https://codecov.io/gh/alvarob96/pyrtfolio)

## Introduction

**pyrtfolio** is a Python package created based on [investpy](https://github.com/alvarobartt/investpy) data which
aims to create custom stock portfolios. In investment, a portfolio is a grouping of financial assets as well as their
fund counterparts; note that a portfolio can also consist of non-publicly tradable securities. So on, **investpy** data 
will be used to create custom portfolios from the data provided by the user such as the asset symbol, purchase date, 
number of bought shares, etc.

## Installation

In order to get this package working you will need to install **pyrtfolio** via pip by typing the following 
command in the terminal:

``$ pip install pyrtfolio==0.2``

Every package used is listed in [requirements.txt](https://github.com/alvarobartt/pyrtfolio/blob/master/requirements.txt) 
file, which can also be installed via pip:

``$ pip install -r requirements.txt``

## Usage

Currently, **pyrtfolio** can just be used for generating stock portfolios, so on, an example is proposed below
which creates a new portfolio and adds some equities/stocks. Note that the returned portfolio is a :obj:`pandas.DataFrame`,
but the package is intended to generate either a CVS or a XLSX file.

```python
from pyrtfolio.StockPortfolio import StockPortfolio

portfolio = StockPortfolio()

portfolio.add_stock(stock_symbol='BBVA',
                    stock_country='spain',
                    purchase_date='04/01/2018',
                    num_of_shares=2,
                    cost_per_share=7.2)

portfolio.add_stock(stock_aymbol='ELE',
                    stock_country='spain',
                    purchase_date='13/06/2019',
                    num_of_shares=15,
                    cost_per_share=23.8)
                    
print(portfolio.data)
```
```{r, engine='python', count_lines}
  stock_symbol stock_name stock_country stock_currency purchase_date  num_of_shares  ...  current_price  gross_current_value  total_dividends  net_current_value  total_gain_loss  total_gain_loss_percentage
0         BBVA       BBVA         spain            EUR    04/01/2018              2  ...          4.716                9.432           5.8788            15.3108           0.9108                    0.06325%
1          ELE     Endesa         spain            EUR    13/06/2019             15  ...         23.500              352.500         326.0250           678.5250         321.5250         0.9006302521008402%
```

## Contribute

As this is an open source project it is open to contributions, bug reports, bug fixes, documentation improvements, 
enhancements and ideas.

Also there is an open tab of [issues](https://github.com/alvarobartt/pyrtfolio/issues) where anyone can 
contribute opening new issues if needed or navigate through them in order to solve them or contribute to its solving. 
Remember that issues are not threads to describe multiple issues, this does not mean that issues can't be discussed, 
but if new issues are reported, a new issue should be open so to keep a structured project management.
