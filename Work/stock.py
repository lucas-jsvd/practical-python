class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        self.custo = self.shares * self.price
        return self.custo

    def sell(self, num_venda):
        self.shares -= num_venda
        return self.shares
