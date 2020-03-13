Usage
=====

**pyrtfolio** usage is pretty simple, since until the current release (0.1), just the StockPortfolios are
available with the basic data. So on, the one and only usage that can be currently done with this package consists on
generating portfolios for the introduced stocks.

An example will be presented below to show the user how to use the package to generate his/her custom stock portfolios.

.. codeauthor:: Alvaro Bartolome @ alvarobartt in GitHub
.. code-block:: python

    from pyrtfolio.StockPortfolio import StockPortfolio

    portfolio = StockPortfolio()

    portfolio.add_stock(stock_name='bbva',
                        stock_country='spain',
                        purchase_date='04/01/2018',
                        num_of_shares=2,
                        cost_per_share=7.2)

    portfolio.add_stock(stock_name='endesa',
                        stock_country='spain',
                        purchase_date='13/06/2019',
                        num_of_shares=15,
                        cost_per_share=23.8)

    print(portfolio.data)

Which outputs the following stock portfolio::

      stock_name stock_country purchase_date  num_of_shares  cost_per_share  current_price  gross_current_value
    0       bbva         spain    04/01/2018              2             7.2          4.597                9.194
    1     endesa         spain    13/06/2019             15            23.8         23.890              358.350

Further usage will be documented whenever the package is updated with new features. Make sure to watch and star the repo
to be notified about all conversations!