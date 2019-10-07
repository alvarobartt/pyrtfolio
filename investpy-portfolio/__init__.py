#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

__author__ = "Alvaro Bartolome @ alvarob96 in GitHub"
__version__ = "0.1"


portfolio = StockPortfolio()

portfolio.add_stock(stock_name='bbva',
                    stock_country='spain',
                    purchase_date='04/01/2018',
                    num_of_shares=2,
                    cost_per_share=7.2)

print(portfolio.data.head())
