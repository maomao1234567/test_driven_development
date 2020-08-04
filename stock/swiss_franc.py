from stock.money import Money


class SwissFranc(Money):

    def times(self, stock_amount):
        amount = self._amount * stock_amount
        return SwissFranc(amount)
