# 在假设已经给定汇率的情况下，要能对两种不同的币种金额相加，并将结果转换为某一种币种；
# 要将某一金额与某一个数相乘，并得到一个总金额
from stock.dollar import Dollar
from stock.swiss_franc import SwissFranc
from stock.money import Money


def test_multi_stock_price():
    five = Dollar(5)
    ten = five.times(2)
    assert ten.amount == 10
    fifteen = five.times(3)
    assert fifteen.amount == 15


def test_same_currency():
    five_dollar1 = Dollar(5)
    five_dollar2 = Dollar(5)

    assert five_dollar1 == five_dollar2

    six_dollar = Dollar(6)
    assert five_dollar1 != six_dollar


def test_swiss_franc():
    five_swiss_franc = SwissFranc(5)

    assert five_swiss_franc.amount == 5


def test_swiss_franc_multi_amount():
    five_swiss_franc = SwissFranc(5)

    ten_swiss_franc = five_swiss_franc.times(2)
    assert ten_swiss_franc.amount == 10

    fifteen_swiss_franc = five_swiss_franc.times(3)
    assert fifteen_swiss_franc == SwissFranc(15)


def test_two_currency_is_same():
    five_dollar = Dollar(5)
    five_swiss_franc = SwissFranc(5)

    assert five_dollar != five_swiss_franc


def test_currency_name():
    five_dollar = Dollar(5)
    five_swiss_franc = SwissFranc(5)

    assert five_dollar.currency == 'USD'
    assert five_swiss_franc.currency == 'CHF'


def test_the_same_money_add():
    five_dollar = Dollar(5)
    ten_dollar = Dollar(10)

    assert five_dollar.plus(ten_dollar) == Dollar(15)


def test_the_diff_money_add():
    five_dollar = Dollar(5)
    five_swiss_franc = SwissFranc(10)

    assert five_dollar.plus(five_swiss_franc) == Dollar(10)
