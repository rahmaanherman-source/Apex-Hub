from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/health")
async def dashboard_health():
    return {"status": "ok", "service": "dashboard"}
