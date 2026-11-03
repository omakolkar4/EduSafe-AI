
import re

# Detect common prompt-injection patterns
BLOCKED_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"reveal\s+(the\s+)?system\s+prompt",
    r"show\s+(me\s+)?(all\s+)?(private|confidential)\s+data",
    r"reveal\s+(all\s+)?student\s+records",
    r"bypass\s+(all\s+)?safety",
    r"act\s+as\s+an\s+unrestricted"
]

def check_input(user_input):
    if not user_input or not user_input.strip():
        return False, "Please enter a question."

    if len(user_input) > 2000:
        return False, "Input is too long. Maximum 2000 characters."

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return False, "Potential prompt injection detected. Request blocked."

    return True, "Input passed safety checks."
