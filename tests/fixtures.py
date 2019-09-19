QUERY_LINK = """
query {
  calculatePrice($margin: Float, $exchangeRate: String, $saleType:Enum)
}
"""


# mutation CreateLink($url: String!, $desc: String!){
#   createLink(description: $desc, url: $url){
#     id,
#     url,
#     description
#   }
# }