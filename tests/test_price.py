from buy_coins.schema import schema
from graphene.test import Client
# import sys

# sys.path.append('.')
# from os import path
# schema = path('buy_coins.schema')


def test_get_buy_price():
    """Test to know how much to buy bitcoin in Naira"""

    client = Client(schema)
    executed = client.execute(
        '''query{calculatePrice(margin: 1.2, exchangeRate: "USD/NGN", saleType:buy)}''',)

    price_in_naira = executed["data"]["calculatePrice"]
    assert executed == {
        "data": {
            "calculatePrice": price_in_naira
        }
    }


def test_get_sell_price():
    """Test to know how much to sell bitcoin in Naira"""

    client = Client(schema)
    executed = client.execute(
        '''query{calculatePrice(margin: 1.2, exchangeRate: "USD/NGN", saleType:sell)}''',)

    price_in_naira = executed["data"]["calculatePrice"]
    assert executed == {
        "data": {
            "calculatePrice": price_in_naira
        }
    }


def test_to_check_for_improper_exchangeRate():
    """Test for failure if exchangeRate is provided with a wrong value"""
    client = Client(schema)
    executed = client.execute(
        '''query{calculatePrice(margin: 1.2, exchangeRate: "USD", saleType: sell)}''',)

    assert executed["errors"][0]["message"] == 'exchange rate can only be in "USD/NGN" format'


def test_to_check_for_improper_margin():
    """Test for failure if exchangeRate is provided with a wrong value"""
    client = Client(schema)
    executed = client.execute(
        '''query{calculatePrice(margin: 0, exchangeRate: "USD/NGN", saleType: sell)}''',)

    assert executed["errors"][0]["message"] == 'please provide a margin or a proper value'
