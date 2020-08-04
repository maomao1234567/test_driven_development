class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other.amount and type(self) == type(other)

    @property
    def amount(self):
        return self._amount

    def times(self, stock_amount):
        raise NotImplementedError
