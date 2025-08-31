# app/routes/domain_routes.py
from fastapi import APIRouter, HTTPException
from app.models.schemas import DomainCheckRequest, DomainCheckResponse, SuggestDomainsResponse
from app.services.epp_client import epp_client
from app.utils.helpers import normalize_domain, is_valid_ke_domain, generate_suggestions
from datetime import datetime
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/check-domain", response_model=DomainCheckResponse, tags=["Domain"])
async def check_domain(req: DomainCheckRequest):
    domain = normalize_domain(req.domain)
    if not is_valid_ke_domain(domain):
        raise HTTPException(status_code=400, detail="Invalid .ke domain format")
    try:
        available = await epp_client.check_domain_availability_async(domain)
        return DomainCheckResponse(
            available=available,
            domain=domain,
            registrar_url="https://www.kenic.or.ke/registrars",
            checked_at=datetime.utcnow().isoformat() + "Z"
        )
    except Exception as e:
        logger.exception("Domain check failed")
        raise HTTPException(status_code=500, detail="Failed to check domain availability")

@router.post("/suggest-domains", response_model=SuggestDomainsResponse, tags=["Domain"])
async def suggest_domains(req: DomainCheckRequest):
    base = normalize_domain(req.domain).replace(".ke", "")
    candidates = generate_suggestions(base, count=7)
    available = []
    for s in candidates:
        try:
            ok = await epp_client.check_domain_availability_async(s)
            if ok:
                available.append(s)
        except Exception:
            logger.exception("Suggestion check failed for %s", s)
    return SuggestDomainsResponse(original_domain=req.domain, suggestions=available[:5])

