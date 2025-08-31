# app/services/db_service.py
import sqlite3
from contextlib import contextmanager
import os
import logging

logger = logging.getLogger(__name__)

DEFAULT_REGISTRARS =[
(
      "Truehost Cloud Limited",
      "+25420 790 3111",
     "info@truehost.co.ke",
    "http://www.truehost.co.ke/",
    "https://kenic.or.ke/wp-content/uploads/2023/05/truehost1.png"
    "description not available at the moment"
  ),
  (
      "Kenya Website Experts",
      "0722 209 414",
     "info@kenyawebexperts.co.ke",
    "https://kenyawebexperts.co.ke/",
    "https://kenic.or.ke/wp-content/uploads/2023/05/kwe.png"
    "description not available at the moment"
  ),
  (
      "HostPinnacle Cloud Limited",
      "0111054710",
     "info@hostpinnacle.co.ke",
    "https://www.hostpinnacle.co.ke/",
    "https://kenic.or.ke/wp-content/uploads/2023/05/HP-1.png"
    "description not available at the moment"
  ),
  (
      "HostAfrica EAC",
      "0709 399 000",
     "support@hostafrica.com",
    "https://www.hostafrica.ke/kenic-registrar/",
    "https://kenic.or.ke/wp-content/uploads/2023/06/HA.jpg"
    "description not available at the moment"
  )
]
DB_PATH = None

def init_db(path: str = "domain_app.db"):
    global DB_PATH
    DB_PATH = path
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS registrars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            website TEXT NOT NULL,
            logo_url TEXT NOT NULL
        )
    """)
    cur.execute("SELECT COUNT(*) FROM registrars")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO registrars (name, phone, email, website, logo_url) VALUES (?, ?, ?,>
        conn.commit()
        logger.info("Inserted default registrars")
    conn.close()

@contextmanager
def get_db():
    global DB_PATH
    if not DB_PATH:
        DB_PATH = os.getenv("DATABASE_PATH", "domain_app.db")
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()
