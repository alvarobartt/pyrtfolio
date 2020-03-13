# Copyright 2019 Alvaro Bartolome @ alvarobartt in GitHub
# See LICENSE for details.

import datetime

import investpy


class Stock(object):
    """ Stock is a support class of `pyrtfolio` which validates the Stocks before adding them to StockPortfolio.

    This class is a support class to validate the Stocks before finally adding them to the portfolio created in
    StockPortfolio since the historical data of the introduced Stock needs to be retrieved and, so on, it will error
    if the introduced Stock is not valid.

    Attributes:
        stock_symbol (:obj:`str`): symbol of the Stock that is going to be added to the StockPortfolio.
        stock_country (:obj:`str`): country from where the specified stock_symbol is, so to validate it.
        purchase_date (:obj:`str`):
            date when the shares of the introduced stock were bought, formatted as dd/mm/yyyy.
        num_of_shares (:obj:`int`): amount of shares bought of the specified Stock in the specified date.
        cost_per_share (:obj:`float`): price of every share of the Stock in the specified date.
        valid (:obj:`boolean`): either True or False if the Stock is valid or not, respectively.

    """

    def __init__(self, stock_symbol, stock_country, purchase_date, num_of_shares, cost_per_share):
        """ This is the init method of Stock class which is launched every time the user instances it.

        This method is the init method of this class, Stock, and its main function is to init all the attributes
        contained in it, as previously defined when the function `add_stock()` was called from StockPortfolio. The
        specified values in this class are going to be accessed through the self operator whenever the validation
        function is called, since it is the main function of this class, validating Stocks.

        Args:
            stock_symbol (:obj:`str`): symbol of the Stock that is going to be added to the StockPortfolio.
            stock_country (:obj:`str`): country from where the specified stock_symbol is, so to validate it.
            purchase_date (:obj:`str`):
                date when the shares of the introduced stock were bought, formatted as dd/mm/yyyy.
            num_of_shares (:obj:`int`): amount of shares bought of the specified Stock in the specified date.
            cost_per_share (:obj:`float`): price of every share of the Stock in the specified date.

        """
        self.stock_symbol = stock_symbol
        self.stock_country = stock_country
        self.purchase_date = purchase_date
        self.num_of_shares = num_of_shares
        self.cost_per_share = cost_per_share

        self.valid = False

    def validate(self):
        """ Method used to validate that the introduced Stock is valid before adding it to the StockPortfolio.

        This method is the one in charge of the validation of the introduced Stock via checking the introduced data
        with the one indexed in investpy, so to check if the data match. Also, the introduced parameters are checked in
        order to determine if the type is correct of those values is correct, if not, an exception will be raised. The
        result of this function is just setting either True or False to the self.valid value if the Stock is valid or
        not, respectively.

        """
        if not isinstance(self.stock_symbol, str):
            raise ValueError("ERROR [0005]: The introduced stock_symbol is mandatory and should be a str.")

        if not isinstance(self.stock_country, str):
            raise ValueError("ERROR [0006]: The introduced stock_country is mandatory and should be a str.")

        try:
            datetime.datetime.strptime(self.purchase_date, '%d/%m/%Y')
        except ValueError:
            raise ValueError("ERROR [0007]: The introduced purchase_date is not properly formatted (dd/mm/yyyy).")

        purchase_date_ = datetime.datetime.strptime(self.purchase_date, '%d/%m/%Y')
        if purchase_date_ > datetime.datetime.now():
            raise ValueError("ERROR [0008]: The introduced purchase_date is not valid since it should be earlier than "
                             "the current date.")

        if not isinstance(self.num_of_shares, int):
            raise ValueError("ERROR [0009]: The introduced num_of_shares is mandatory and should be an int higher "
                             "than 0.")
        else:
            if self.num_of_shares <= 0:
                raise ValueError("ERROR [0009]: The introduced num_of_shares is mandatory and should be an int higher "
                                 "than 0.")

        if not isinstance(self.cost_per_share, float):
            raise ValueError("ERROR [0010]: The introduced cost_per_share is mandatory and should be a float higher "
                             "than 0.")
        else:
            if self.cost_per_share <= 0:
                raise ValueError("ERROR [0010]: The introduced Stock is not valid.")

        stock_countries = investpy.get_stock_countries()

        if self.stock_country.lower() in stock_countries:
            stocks = investpy.get_stocks(country=self.stock_country)

            search_results = stocks[stocks['symbol'].str.lower() == self.stock_symbol.lower()]

            if len(search_results) > 0:
                data = investpy.get_stock_historical_data(stock=self.stock_symbol,
                                                          country=self.stock_country,
                                                          from_date=self.purchase_date,
                                                          to_date=datetime.date.today().strftime("%d/%m/%Y"))

                try:
                    purchase_date_ = purchase_date_.strftime("%Y-%m-%d")
                    min_value = data.loc[purchase_date_]['Low']
                    max_value = data.loc[purchase_date_]['High']
                except KeyError:
                    raise KeyError("ERROR [0004]: The introduced purchase_date is not valid since the market was "
                                   "closed.")

                if min_value <= self.cost_per_share <= max_value:
                    self.valid = True
                else:
                    raise ValueError("ERROR [0011]: The introduced value is not possible, because the range stock "
                                     "values of the purchase data were between " + str(min_value) + " and " + str(max_value))
            else:
                raise ValueError("ERROR [0003]: No results were found for the introduced stock_symbol in the specified "
                                 "stock_country.")
        else:
            raise ValueError("ERROR [0002]: The introduced stock_country is not valid or does not have any indexed "
                             "stock.")
