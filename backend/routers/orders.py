from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("")
async def list_orders():
    return {"items": [], "count": 0, "source": "backend"}

@router.get("/health")
async def orders_health():
    return {"status": "ok", "service": "orders"}
