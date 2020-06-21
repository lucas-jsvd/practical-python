# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    compras_totais = 0.0
    with open(filename, "rt") as arquivo:
        csvfile = csv.reader(arquivo)
        headers = next(csvfile)
        for num_linha, linha in enumerate(csvfile, start=1):
            record = dict(zip(headers, linha))
            try:
                quant_acao = int(record["shares"])
                preco_acao = float(record["price"])
                valor_total_acao = quant_acao * preco_acao
                compras_totais += valor_total_acao
            except ValueError:
                print(f'Row {num_linha}: Couldn\'t convert: {linha}')
    return compras_totais


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Work/Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total do custo {cost:.2f}")
