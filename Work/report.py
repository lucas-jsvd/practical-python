# report.py
#
# Exercise 2.4
import sys

from fileparse import parse_csv
from portfolio import Portfolio
from stock import Stock
from tableformat import create_formatter


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, "rt") as f:
        portfolio_dict = parse_csv(
            f, select=["name", "shares", "price"], types=[str, int, float])
        portfolio_classe = [
            Stock(row["name"], row["shares"], row["price"]) for row in portfolio_dict]
    return Portfolio(portfolio_classe)


def read_prices(filename):
    with open(filename, "rt") as f:
        price = dict(parse_csv(f, has_headers=False, types=[str, float]))
    return price


def make_report(portfolio, precos):
    lista_acoes = []
    for acao in portfolio:
        diferencia_preco = precos[acao.name] - (acao.price)
        lista_acoes.append(
            (acao.name, acao.shares, precos[acao.name], diferencia_preco))
    return lista_acoes


def print_report(reportdata, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    # Create the report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    main(sys.argv)
