# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    compras_totais = 0.0
    with open(filename, "rt") as arquivo:
        csvfile = csv.reader(arquivo)
        next(csvfile)
        for linha in csvfile:
            try:
                quant_acao = int(linha[1])
                preco_acao = float(linha[2])
            except ValueError:
                print("Existem valores vazios ou passados em um formato incorreto.")
            valor_total_acao = quant_acao * preco_acao
            compras_totais += valor_total_acao
    return compras_totais


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Work/Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total do custo {cost:.2f}")
