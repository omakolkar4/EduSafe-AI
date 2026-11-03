import re

INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"reveal\s+(the\s+)?system\s+prompt",
    r"reveal\s+(all\s+)?private\s+student",
    r"system\s+override",
    r"bypass\s+(all\s+)?safety"
]


def check_study_content(content):

    if not content or not content.strip():
        return False, "Study material cannot be empty."

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return False, (
                "Untrusted content warning: Malicious instructions "
                "were detected in the supplied study material."
            )

    return True, "Study content passed safety checks."