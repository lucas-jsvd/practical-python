# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    '''Faz a leitura do portifolio do usuario no arquivo indicado.'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        cabecalho = next(rows)
        for number_row, row in enumerate(rows, start=1):
            holding = dict(zip(cabecalho, row))
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    '''Faz a leitura dos preços atuais das ações do usuario no arquivo
    indicado.'''
    acoes = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        try:
            for acao, valor in rows:
                acoes[acao] = float(valor)
        except ValueError:
            pass
    return acoes


def make_report(portfolio, acoes):
    lista_acoes = []
    for linha in portfolio:
        diferencia_preco = acoes[linha["name"]] - float(linha["price"])
        lista_acoes.append((linha["name"], linha["shares"], acoes[linha["name"]], diferencia_preco))
    return lista_acoes


def print_report(report):
    cabecalho = ("Name", "Shares", "Price", "Change")    
    print(f'{cabecalho[0]:>10s} {cabecalho[1]:>10s} {cabecalho[2]:>10s} {cabecalho[3]:>10s}')
    print("---------- " * 4)
    for name, shares, price, change in report:
        print(f'{name:>10s} {int(shares):>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename, price_filename):
    report = make_report(read_portfolio(portfolio_filename),read_prices(price_filename))
    print_report(report)


portfolio_report("Work\\Data\\portfoliodate.csv", "Work\\Data\\prices.csv")
