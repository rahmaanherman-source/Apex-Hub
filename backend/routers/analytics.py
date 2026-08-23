from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/health")
async def analytics_health():
    return {"status": "ok", "service": "analytics"}

@router.get("/summary")
async def analytics_summary():
    return {"status": "available", "source": "backend", "metrics": {}}
