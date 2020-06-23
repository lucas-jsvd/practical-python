# pcost.py
#
# Exercise 1.27
from stock import Stock
from fileparse import parse_csv
import sys
import report


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    cost = portfolio_cost(args[1])
    print(f"Total do custo: {cost:.2f}")


if __name__ == "__main__":
    main(sys.argv)
