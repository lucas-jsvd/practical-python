# pcost.py
#
# Exercise 1.27
from stock import Stock
from fileparse import parse_csv
import sys


def portfolio_cost(filename):
    compras_totais = 0.0
    with open(filename, "rt") as f:
        lista_dict = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float])
        lista_obj = [Stock(dici["name"], dici["shares"], dici["price"]) for dici in lista_dict]
        compras_totais = sum([obj.cost for obj in lista_obj])
    return compras_totais


def main(args):
    cost = portfolio_cost(args[1])
    print(f"Total do custo: {cost:.2f}")


if __name__ == "__main__":
    main(sys.argv)
