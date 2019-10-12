#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

import investpy_portfolio
from investpy_portfolio.StockPortfolio import StockPortfolio


def test_package():
    """
    This function tests both the authorship and version of investpy_portfolio.
    """

    print(investpy_portfolio.__author__)
    print(investpy_portfolio.__version__)


def test_stock_portfolio():
    """
    This functions tests the basic creation of a StockPortfolio with some sample Stocks.
    """

    portfolio = StockPortfolio()

    portfolio.add_stock(stock_symbol='BBVA',
                        stock_country='spain',
                        purchase_date='04/01/2018',
                        num_of_shares=2,
                        cost_per_share=7.2)

    portfolio.add_stock(stock_symbol='ELE',
                        stock_country='spain',
                        purchase_date='13/06/2019',
                        num_of_shares=15,
                        cost_per_share=23.8)

    print(portfolio.data.head())
    portfolio.refresh()
    print(portfolio.data.head())


if __name__ == '__main__':
    test_package()
    test_stock_portfolio()
