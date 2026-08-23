from fastapi import APIRouter

router = APIRouter(prefix="/customer", tags=["customer"])

@router.get("/health")
async def customer_health():
    return {"status": "ok", "service": "customer"}
