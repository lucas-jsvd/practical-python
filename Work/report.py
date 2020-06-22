# report.py
#
# Exercise 2.4
from stock import Stock
from fileparse import parse_csv
import sys


def read_portfolio(filename):
    with open(filename, "rt") as f:
        portfolio_dict = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float])
        portfolio_classe = [Stock(row["name"], row["shares"], row["price"]) for row in portfolio_dict]
    return portfolio_classe


def read_prices(filename):
    with open(filename, "rt") as f:
        price = dict(parse_csv(f, has_headers=False, types=[str, float]))
    return price


def make_report(portfolio, precos):
    lista_acoes = []
    for acao in portfolio:
        diferencia_preco = precos[acao.name] - (acao.price)
        lista_acoes.append((acao.name, acao.shares, precos[acao.name], diferencia_preco))
    return lista_acoes


def print_report(report):
    cabecalho = ("Name", "Shares", "Price", "Change")    
    print(f'{cabecalho[0]:>10s} {cabecalho[1]:>10s} {cabecalho[2]:>10s} {cabecalho[3]:>10s}')
    print("---------- " * 4)
    for name, shares, price, change in report:
        print(f'{name:>10s} {(shares):>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename, price_filename):
    report = make_report(read_portfolio(portfolio_filename), read_prices(price_filename))
    print_report(report)


def main(args):
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    main(sys.argv)
