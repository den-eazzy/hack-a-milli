# app/main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

load_dotenv()  # loads .env

from app.services.db_service import init_db
from app.services.epp_client import epp_client
from app.routes.domain_routes import router as domain_router
from app.routes.registrars_routes import router as registrars_router
from app.routes.chatbot_routes import router as chatbot_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dotke")

app = FastAPI(title="DotKE .KE Domain Search API", version="1.0.0")

# CORS - restrict in production via ALLOWED_ORIGINS env
allowed_origins = os.getenv("ALLOWED_ORIGINS", "")
origins = [o.strip() for o in allowed_origins.split(",")] if allowed_origins else ["http://localhost:808>
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(domain_router)
app.include_router(registrars_router)
app.include_router(chatbot_router)

@app.on_event("startup")
async def startup():
    # init DB and connect EPP
    db_path = os.getenv("DATABASE_PATH", "domain_app.db")
    init_db(db_path)
    await epp_client.connect()
    logger.info("DotKE backend started")
