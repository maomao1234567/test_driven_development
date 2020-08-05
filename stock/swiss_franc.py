from stock.money import Money


class SwissFranc(Money):
    def __init__(self, amount):
        super(SwissFranc, self).__init__(amount)
        self._currency = 'CHF'

    def times(self, stock_amount):
        amount = self._amount * stock_amount
        return SwissFranc(amount)
