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


def ganhos_perda(portfolio, acoes):
    diferencia_total = 0.0
    print("Nome\tPreco Compra\tQuantidade\tTotal da Compra\t\tPreco de Venda\t\tTotal de Venda\t\tGanho/Perda")
    for acao in portfolio:
        valor_acao_compra = acao["shares"] * acao["price"]
        valor_acao_atual = acao["shares"] * float(acoes[acao["name"]])
        diferencia = valor_acao_atual - valor_acao_compra
        diferencia_total += diferencia
        print(f'{acao["name"]:<4s} {acao["price"]:^16.2f} {acao["shares"]:^16d} {valor_acao_compra:^18.2f} {acoes[acao["name"]]:^26.2f} {valor_acao_atual:^21.2f} {diferencia:^21.2f}')
    print(f"Total de ganhos/perdas: {diferencia_total:>97.2f}")


def make_report(portfolio, acoes):
    lista_acoes = []
    for linha in portfolio:
        diferencia_preco = acoes[linha["name"]] - float(linha["price"])
        lista_acoes.append((linha["name"], linha["shares"], acoes[linha["name"]], diferencia_preco))
    return lista_acoes


report = make_report(read_portfolio("Work\\Data\\portfoliodate.csv"), read_prices("Work\\Data\\prices.csv"))
cabecalho = ("Name", "Shares", "Price", "Change")
print(f'{cabecalho[0]:>10s} {cabecalho[1]:>10s} {cabecalho[2]:>10s} {cabecalho[3]:>10s}')
print("---------- " * 4)
for name, shares, price, change in report:
    print(f'{name:>10s} {int(shares):>10d} {price:>10.2f} {change:>10.2f}')
