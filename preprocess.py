import re

ALIASES = {
    "INFY": "INFOSYS",
    "TCS": "TATA CONSULTANCY SERVICES",
    "L&T": "LARSEN TOUBRO",
    "LT": "LARSEN TOUBRO"
}

REPLACEMENTS = {
    "PVT": "PRIVATE",
    "PVT.": "PRIVATE",
    "LTD": "LIMITED",
    "LTD.": "LIMITED",
    "CO": "COMPANY",
    "CO.": "COMPANY",
    "TECH": "TECHNOLOGIES",
    "SVCS": "SERVICES",
    "INTL": "INTERNATIONAL",
    "&": "AND"
}

def normalize_text(text: str) -> str:
    if not text:
        return ""

    text = str(text).upper().strip()

    # normalize unicode apostrophes / quotes
    text = text.replace("’", "'").replace("`", "'")

    # alias replacement first
    for key, value in ALIASES.items():
        text = re.sub(rf"\b{re.escape(key)}\b", value, text)

    # keep letters/numbers/spaces/& only
    text = re.sub(r"[^\w\s&]", " ", text)

    # standard replacements
    for key, value in REPLACEMENTS.items():
        text = re.sub(rf"\b{re.escape(key)}\b", value, text)

    # normalize &
    text = text.replace("&", " AND ")

    # collapse spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text