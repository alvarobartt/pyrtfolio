#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

import datetime

import investpy


class Stock(object):
    """
    This class ...
    """

    def __init__(self, stock_name, stock_country, purchase_date, num_of_shares, cost_per_share):
        self.stock_name = stock_name
        self.stock_country = stock_country
        self.purchase_date = purchase_date
        self.num_of_shares = num_of_shares
        self.cost_per_share = cost_per_share

        self.valid = False

    def validate(self):
        """
        This function ...
        """

        if not isinstance(self.stock_name, str):
            return
        if not isinstance(self.stock_country, str):
            return
        try:
            datetime.datetime.strptime(self.purchase_date, '%d/%m/%Y')
        except ValueError:
            return
        purchase_date_ = datetime.datetime.strptime(self.purchase_date, '%d/%m/%Y')
        if purchase_date_ > datetime.datetime.now():
            return
        if not isinstance(self.num_of_shares, int):
            return
        else:
            if self.num_of_shares <= 0:
                return
        if not isinstance(self.cost_per_share, float):
            return
        else:
            if self.cost_per_share <= 0:
                return
        stock_countries = investpy.get_equity_countries()
        if self.stock_country.lower() in stock_countries:
            stocks = investpy.get_equities(country=self.stock_country)
            search_results = stocks[stocks['name'].str.lower() == self.stock_name.lower()]
            if len(search_results) > 0:
                data = investpy.get_historical_data(equity=self.stock_name,
                                                    country=self.stock_country,
                                                    from_date=self.purchase_date,
                                                    to_date=datetime.date.today().strftime("%d/%m/%Y"))

                try:
                    purchase_date_ = purchase_date_.strftime("%Y-%m-%d")
                    open_value = data.loc[purchase_date_]['Open']
                    close_value = data.loc[purchase_date_]['Close']
                except KeyError:
                    return

                if open_value <= self.cost_per_share <= close_value:
                    self.valid = True
