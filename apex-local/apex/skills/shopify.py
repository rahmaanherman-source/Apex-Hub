import requests
from apex.config import env
API_VERSION='2024-10'
def _url():return f"https://{env('SHOPIFY_STORE_DOMAIN')}/admin/api/{API_VERSION}/graphql.json"
def _headers():return {'X-Shopify-Access-Token':env('SHOPIFY_ADMIN_TOKEN'),'Content-Type':'application/json'}
def productSet(input):
 q='mutation productSet($input: ProductSetInput!){productSet(input:$input){product{id title} userErrors{field message}}}'
 return requests.post(_url(),json={'query':q,'variables':{'input':input}},headers=_headers(),timeout=30).json()
def getOrders(first=10):
 q='query($first:Int!){orders(first:$first,sortKey:CREATED_AT,reverse:true){edges{node{id name totalPriceSet{shopMoney{amount currencyCode}}}}}}'
 return requests.post(_url(),json={'query':q,'variables':{'first':first}},headers=_headers(),timeout=30).json()
