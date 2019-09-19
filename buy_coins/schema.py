import graphene
import buy_coins.coins.schema


class Query(
        buy_coins.coins.schema.Query,
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)