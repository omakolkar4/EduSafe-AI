
import re

SENSITIVE_PATTERNS = [
    r"\b(?:student|students)\b.*\b(?:passwords?|phone numbers?|emails?|addresses?|marks|records|details|data)\b",
    r"\b(?:passwords?|phone numbers?|emails?|addresses?|marks|records|details|data)\b.*\b(?:student|students)\b",
    r"\b(?:another|other)\s+student(?:'s)?\b.*\b(?:records|marks|details|data)\b"
]

def check_privacy(text):
    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False, (
                "Privacy Protection: Request for sensitive student "
                "information blocked."
            )

    return True, "Privacy check passed."
