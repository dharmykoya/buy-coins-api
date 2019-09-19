from graphene import ObjectType, String, Boolean, ID, Field, Int, List, Float, Enum, Argument
import requests
import json
from graphql import GraphQLError


class PriceType(ObjectType):
    code = String()
    rate = Float()
    margin = Float()
    exchangeRate = String()
    calculatePrice = Float()
    new_rate = Float()


class SaleType(Enum):
    buy = "buy"
    sell = "sell"



class Query(ObjectType):
    calculate_price = Float(margin=Float(), exchangeRate=String(
    ), saleType=Argument(SaleType, required=True))

    def resolve_calculate_price(self, info, **kwargs):
        margin = kwargs.get('margin')
        exchangeRate = kwargs.get('exchangeRate')
        saleType = kwargs.get('saleType')

        if exchangeRate != "USD/NGN":
            raise GraphQLError('exchange rate can only be in "USD/NGN" format')

        if not margin:
            raise GraphQLError('please provide a margin or a proper value')

        request_from_coindesk = requests.get(
            url='https://api.coindesk.com/v1/bpi/currentprice.json')
        json_result_from_coindesk = json.dumps(request_from_coindesk.text)
        coindesk_result = json.loads(json_result_from_coindesk)
        result = json.loads(coindesk_result)

        rate_to_calculate = result["bpi"]["USD"]["rate_float"]

        if saleType == SaleType.sell:
            calculated_value = (margin/100) * rate_to_calculate
            new_rate = (rate_to_calculate - calculated_value) * 360
            return new_rate
        elif saleType == SaleType.buy:
            calculated_value = (margin/100) * rate_to_calculate
            new_rate = (rate_to_calculate - calculated_value) * 360
            return new_rate
        else:
            raise GraphQLError('please saleType can either be buy or sell')
