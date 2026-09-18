from fastapi import APIRouter

from src.db.session import check_database_connection

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    db_status = "connected"

    try:
        await check_database_connection()
    except Exception:
        db_status = "disconnected"

    return {
        "status": "healthy",
        "service": "Aegis",
        "database": db_status,
        "version": "0.1.0",
    }