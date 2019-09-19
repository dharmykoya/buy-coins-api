from graphene.test import Client
from buy_coins.schema import schema


def test_hey():
    client = Client(schema)
    executed = client.execute('''calculatePrice(margin, exchangeRate, saleType)''', context={
                              'margin': '1.2', 'exchangeRate': 'USD', 'saleType': 'sell'})
    assert executed == {
        "data": {
            "calculatePrice": 3624484.7302560005
        }
    }
