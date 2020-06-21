# pcost.py
#
# Exercise 1.27
from fileparse import parse_csv
import sys


def portfolio_cost(filename):
    compras_totais = 0.0
    csvfile = parse_csv(filename, select=["shares", "price"], types=[int, float])
    compras_totais = sum([(acao["shares"] * acao["price"]) for acao in csvfile])
    return compras_totais


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total do custo: {cost:.2f}")
