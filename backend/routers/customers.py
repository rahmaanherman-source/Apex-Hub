from fastapi import APIRouter

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("")
async def list_customers():
    return {"items": [], "count": 0, "source": "backend"}

@router.get("/health")
async def customers_health():
    return {"status": "ok", "service": "customers"}
