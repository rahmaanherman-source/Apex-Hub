from fastapi import APIRouter

router = APIRouter(prefix="/merchant", tags=["merchant"])

@router.get("/health")
async def merchant_health():
    return {"status": "ok", "service": "merchant"}
