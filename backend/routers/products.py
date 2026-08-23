from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get("")
async def list_products():
    return {"items": [], "count": 0, "source": "backend"}

@router.get("/health")
async def products_health():
    return {"status": "ok", "service": "products"}
