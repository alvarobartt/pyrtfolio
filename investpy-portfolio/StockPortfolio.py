#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

from datetime import date

import investpy
import pandas as pd

from .Stock import Stock


class StockPortfolio(object):

    def __init__(self):
        self.stocks = list()
        self.data = None

    def add_stock(self, stock_name, stock_country, purchase_date, num_of_shares, cost_per_share):
        """
        This function ...
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
            print("Introduced Stock is not valid!")

    @staticmethod
    def current_price(data):
        return data.iloc[-1]['Close']

    @staticmethod
    def gross_current_value(current_price, num_of_shares):
        return float(current_price * num_of_shares)

