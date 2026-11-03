
import re

def check_output(response):
    if not response or not response.strip():
        return False, "The AI could not generate a valid response."

    # Prevent accidental exposure of common personal identifiers
    sensitive_patterns = [
        r"\b\d{10}\b",  # Possible phone number
        r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"  # Email address
    ]

    for pattern in sensitive_patterns:
        if re.search(pattern, response):
            return False, "Output blocked because it may contain sensitive information."

    return True, response
