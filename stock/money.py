class Money:
    def __init__(self, amount):
        self._amount = amount
        self._currency = ''

    def __eq__(self, other):
        return self._amount == other.amount and type(self) == type(other)

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    def times(self, stock_amount):
        raise NotImplementedError
