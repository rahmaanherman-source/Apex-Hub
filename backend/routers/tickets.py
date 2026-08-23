from fastapi import APIRouter

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get("")
async def list_tickets():
    return {"items": [], "count": 0, "source": "backend"}

@router.get("/health")
async def tickets_health():
    return {"status": "ok", "service": "tickets"}
