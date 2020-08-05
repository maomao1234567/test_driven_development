from stock.money import Money


class Dollar(Money):

    def __init__(self, amount):
        super(Dollar, self).__init__(amount)
        self._currency = 'USD'

    def times(self, stock_amount):
        amount = self._amount * stock_amount
        return Dollar(amount)
