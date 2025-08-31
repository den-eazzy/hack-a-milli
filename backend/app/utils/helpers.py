# app/utils/helpers.py
import re
from typing import List

DOMAIN_PATTERN = re.compile(r"^[a-zA-Z0-9-]{1,63}\.ke$")

def normalize_domain(input_domain: str) -> str:
    d = input_domain.strip().lower()
    if not d.endswith(".ke"):
        d = f"{d}.ke"
    return d

def is_valid_ke_domain(domain: str) -> bool:
    return bool(DOMAIN_PATTERN.match(domain))

def generate_suggestions(base: str, count: int = 5) -> List[str]:
    b = base.lower().replace(".ke", "")
    candidates = [
        f"{b}ke.ke",
        f"get{b}.ke",
        f"{b}online.ke",
        f"{b}kenya.ke",
        f"my{b}.ke",
        f"{b}app.ke",
        f"{b}hub.ke",
    ]
    return candidates[:count]

