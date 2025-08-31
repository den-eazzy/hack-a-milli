# app/routes/chatbot_routes.py
from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatbotRequest, ChatbotResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

CHATBOT_FAQS = {
    "what is a domain": "A domain name is your website's address on the internet, like 'yourcompany.ke>
    "how to register domain": "Choose a licensed registrar in the app, check availability and follow t>
    "domain cost": "Costs vary by registrar. Expect around KES 1,000–5,000/year for most .ke registrat>
    "domain requirements": ".KE domains are available widely; some 2LDs may have additional rules.",
    "renewal": "Domains are renewed annually or multi-year; use auto-renew to avoid loss.",
    "transfer domain": "Contact the new registrar to initiate transfer; the current registrar can rele>
    "dns": "DNS maps domain names to IP addresses; your registrar or hosting provider can manage DNS r>
    "registrar": "A registrar is an accredited company that registers domains for you."
}

def find_faq_answer(question: str) -> str:
    q = question.lower()
    for k, v in CHATBOT_FAQS.items():
        if any(word in q for word in k.split()):
            return v
    return ("I'm here to help with .ke domain questions. Ask about registration, cost, requirements, o>

@router.post("/chatbot", response_model=ChatbotResponse, tags=["Chatbot"])
def chatbot(req: ChatbotRequest):
    q = req.question.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Question is required")
    try:
        ans = find_faq_answer(q)
        return ChatbotResponse(answer=ans, helpful=True)
    except Exception:
        logger.exception("Chatbot error")
        raise HTTPException(status_code=500, detail="Chatbot service unavailable")

