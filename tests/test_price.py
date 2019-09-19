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
        '''query{calculatePrice(margin: 1.2, exchangeRate: 360, saleType:buy)}''',)

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
        '''query{calculatePrice(margin: 1.2, exchangeRate: 360, saleType:sell)}''',)

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
        '''query{calculatePrice(margin: 1.2, exchangeRate: 0, saleType: sell)}''',)

    assert executed["errors"][0]["message"] == 'please provide a exchangeRate or a proper value'


def test_to_check_for_improper_margin():
    """Test for failure if margin is provided with a wrong value"""
    client = Client(schema)
    executed = client.execute(
        '''query{calculatePrice(margin: 0, exchangeRate: 360, saleType: sell)}''',)

    assert executed["errors"][0]["message"] == 'please provide a margin or a proper value'

def test_to_check_for_exchange_rate_less_than_zero():
    """Test for failure if exchangeRate is provided with a negative value"""
    client = Client(schema)
    executed = client.execute(
        '''query{calculatePrice(margin: 0.4, exchangeRate: -360, saleType: sell)}''',)

    assert executed["errors"][0]["message"] == 'please provide a rate greater than zero' 

def test_to_check_for_margin_less_than_zero():
    """Test for failure if margin is provided with a negative value"""
    client = Client(schema)
    executed = client.execute(
        '''query{calculatePrice(margin: -0.4, exchangeRate: 360, saleType: buy)}''',)

    assert executed["errors"][0]["message"] == 'please provide a margin greater than zero'        
