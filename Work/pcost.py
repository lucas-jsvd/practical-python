# pcost.py
#
# Exercise 1.27
from fileparse import parse_csv
import sys


def portfolio_cost(filename):
    compras_totais = 0.0
    with open(filename, "rt") as f:
        csvfile = parse_csv(f, select=["shares", "price"], types=[int, float])
        compras_totais = sum([(acao["shares"] * acao["price"]) for acao in csvfile])
    return compras_totais


def main(args):
    cost = portfolio_cost(args[1])
    print(f"Total do custo: {cost:.2f}")


if __name__ == "__main__":
    main(sys.argv)
