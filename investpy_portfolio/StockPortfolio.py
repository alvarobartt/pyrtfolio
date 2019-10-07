#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

from datetime import date

import investpy
import pandas as pd

from investpy_portfolio.Stock import Stock


class StockPortfolio(object):
    """ StockPortfolio is the main class of `investpy_portfolio` which is going to manage all the introduced stocks.

    This class is the one that contains the stocks information and the one that will be used by the user in order to
    generate a custom portfolio. So on, this function implements the methods to calculate all the values required in a
    basic portfolio and, as already mentioned, the method to add stocks.

    Attributes:
        stocks (:obj:`list`):
            this list contains all the introduced stocks, which will later be used to generate the portfolio.
        data (:obj:`pandas.DataFrame`): it is the generated portfolio, once the addition of every stock is validated.

    """

    def __init__(self):
        """ This is the init method of StockPortfolio class which is launched every time the user instances it.

        This method is the init method of this class, StockPortfolio, and its main function is to init all the
        attributes contained in it. Every time this class is instanced, the attributes values are restored and, so on,
        the portfolio's data is lost if existing for that instance.

        Note:
            This class does not take any parameters since they are filled once the class is instanced.

        """
        self.stocks = list()
        self.data = None

    def add_stock(self, stock_name, stock_country, purchase_date, num_of_shares, cost_per_share):
        """ Method to add a stock to the portfolio.

        This method adds a stock to the custom portfolio data. Some parameters need to be specified for the introduced
        stock such as the purchase date of the shares, the number of shares bought and the price payed (cost) per every
        share. From this data, the portfolio will be created and the specified calculations will be done, so to give
        the user an overview of his/her own portfolio.

        Args:
            stock_name (:obj:`str`): name of the Stock that is going to be added to the StockPortfolio.
            stock_country (:obj:`str`): country from where the specified stock_name is, so to validate it.
            purchase_date (:obj:`str`):
                date when the shares of the introduced stock were bought, formatted as dd/mm/yyyy.
            num_of_shares (:obj:`int`): amount of shares bought of the specified Stock in the specified date.
            cost_per_share (:obj:`float`): price of every share of the Stock in the specified date.

        """
        stock = Stock(stock_name, stock_country, purchase_date, num_of_shares, cost_per_share)
        stock.validate()

        if stock.valid is True:
            data = investpy.get_historical_data(equity=stock_name,
                                                country=stock_country,
                                                from_date=purchase_date,
                                                to_date=date.today().strftime("%d/%m/%Y"))

            curr_price = self.current_price(data=data)

            obj = {
                'stock_name': stock_name,
                'stock_country': stock_country,
                'purchase_date': purchase_date,
                'num_of_shares': num_of_shares,
                'cost_per_share': cost_per_share,
                'current_price': curr_price,
                'gross_current_value': self.gross_current_value(current_price=curr_price, num_of_shares=num_of_shares),
            }

            self.stocks.append(obj)
            self.data = pd.DataFrame(self.stocks)
        else:
            raise ValueError("ERROR [0001]: The introduced Stock is not valid.")

    @staticmethod
    def current_price(data):
        """
        This method gets the current price value of the introduced stock, which is the last close value indexed in the
        :obj:`pandas.DataFrame`.
        """
        return data.iloc[-1]['Close']

    @staticmethod
    def gross_current_value(current_price, num_of_shares):
        """
        This method calculates the gross current value which is the total current value of the shares bought,
        which is the result of the multiplication of the current price with the number of bought shares.
        """
        return float(current_price * num_of_shares)

