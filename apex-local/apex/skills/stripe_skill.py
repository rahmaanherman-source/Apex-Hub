import stripe
from apex.config import env
def _init():
 stripe.api_key=env('STRIPE_SECRET_KEY')
def createCheckoutSession(amount_cents,product_name,success_url='http://127.0.0.1:8000/success',cancel_url='http://127.0.0.1:8000/cancel'):
 _init();s=stripe.checkout.Session.create(payment_method_types=['card'],line_items=[{'price_data':{'currency':'usd','product_data':{'name':product_name},'unit_amount':amount_cents},'quantity':1}],mode='payment',success_url=success_url,cancel_url=cancel_url);return {'url':s.url,'id':s.id}
def listProducts(limit=10):
 _init();p=stripe.Product.list(limit=limit);return {'data':[{'id':x.id,'name':x.name} for x in p.data]}
