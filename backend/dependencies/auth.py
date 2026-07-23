import stripe, os, httpx
from datetime import datetime

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_...")
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_API_SECRET = os.getenv("SHOPIFY_API_SECRET")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")

async def sync_customer_to_stripe(email: str, name: str) -> dict:
    customers = stripe.Customer.list(email=email, limit=1)
    if customers.data:
        customer = customers.data[0]
        stripe.Customer.modify(customer.id, name=name)
        return {"stripe_id": customer.id}
    customer = stripe.Customer.create(email=email, name=name)
    return {"stripe_id": customer.id}

async def get_shopify_orders(email: str) -> list:
    if not all([SHOPIFY_API_KEY, SHOPIFY_API_SECRET, SHOPIFY_STORE_URL]):
        return []
    auth = (SHOPIFY_API_KEY, SHOPIFY_API_SECRET)
    url = f"https://{SHOPIFY_STORE_URL}/admin/api/2023-10/orders.json?status=any&email={email}&limit=5"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, auth=auth)
        if resp.status_code == 200:
            orders = resp.json().get("orders", [])
            return [{"id": o["id"], "total": o["total_price"], "date": o["created_at"]} for o in orders]
    return []

async def get_customer_lifetime_value(email: str) -> float:
    stripe_customers = stripe.Customer.list(email=email, limit=1)
    if not stripe_customers.data:
        return 0.0
    cus = stripe_customers.data[0]
    charges = stripe.Charge.list(customer=cus.id, limit=100)
    total = sum(ch.amount for ch in charges.auto_paging_iter()) / 100.0
    shopify_orders = await get_shopify_orders(email)
    shopify_total = sum(float(o["total"]) for o in shopify_orders)
    return round(total + shopify_total, 2)