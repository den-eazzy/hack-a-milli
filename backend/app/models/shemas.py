# app/models/schemas.py
from pydantic import BaseModel, HttpUrl
from typing import List

class DomainCheckRequest(BaseModel):
    domain: str

class DomainCheckResponse(BaseModel):
    available: bool
    domain: str
    registrar_url: HttpUrl
    checked_at: str

class Registrar(BaseModel):
    id: int
    name: str
    website: HttpUrl
    email: str
    phone: str
    logo_url: HttpUrl

class ChatbotRequest(BaseModel):
    question: str

class ChatbotResponse(BaseModel):
    answer: str
    helpful: bool

class SuggestDomainsResponse(BaseModel):
    original_domain: str
    suggestions: List[str]
