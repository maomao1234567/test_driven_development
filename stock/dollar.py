from stock.money import Money


class Dollar(Money):

    def times(self, stock_amount):
        amount = self._amount * stock_amount
        return Dollar(amount)
