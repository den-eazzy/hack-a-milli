# app/routes/registrars_routes.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import Registrar
from app.services.db_service import get_db
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/registrars", response_model=List[Registrar], tags=["Registrars"])
def list_registrars():
    try:
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, name, website, email, phone, logo_url FROM registrars ORDER BY nam>
            rows = cur.fetchall()
            res = []
            for r in rows:
                res.append(Registrar(id=r[0], name=r[1], phone=r[2], email=r[3], website=r[4], logo_ur>
            return res
    except Exception:
        logger.exception("Failed to fetch registrars")
        raise HTTPException(status_code=500, detail="Failed to fetch registrar list")

