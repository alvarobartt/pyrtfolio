# Copyright 2019 Alvaro Bartolome @ alvarobartt in GitHub
# See LICENSE for details.

from pyrtfolio.StockPortfolio import StockPortfolio


def test_stock_portfolio_errors():
    """
    This functions tests the errors that can be raised whenever there is an error while creating a StockPortfolio.
    """

    portfolio = StockPortfolio()

    params = [
        {
            'stock_symbol': ['error'],
            'stock_country': 'spain',
            'purchase_date': '04/01/2018',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': ['error'],
            'purchase_date': '04/01/2018',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': 'error',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': '04/01/2050',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': '04/01/2018',
            'num_of_shares': 'error',
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': '04/01/2018',
            'num_of_shares': -7,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': '04/01/2018',
            'num_of_shares': 2,
            'cost_per_share': 'error',
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': '04/01/2018',
            'num_of_shares': 2,
            'cost_per_share': -7,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': '04/01/2018',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'error',
            'purchase_date': '04/01/2018',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'russia',
            'purchase_date': '04/01/2018',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
        {
            'stock_symbol': 'bbva',
            'stock_country': 'spain',
            'purchase_date': '25/12/2018',
            'num_of_shares': 2,
            'cost_per_share': 7.2,
        },
    ]

    for param in params:
        try:
            portfolio.add_stock(stock_symbol=param['stock_symbol'],
                                stock_country=param['stock_country'],
                                purchase_date=param['purchase_date'],
                                num_of_shares=param['num_of_shares'],
                                cost_per_share=param['cost_per_share'])
        except:
            continue


if __name__ == '__main__':
    test_stock_portfolio_errors()
