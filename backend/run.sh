#!/usr/bin/env bash
# run.sh — start dev server (dev only)
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
