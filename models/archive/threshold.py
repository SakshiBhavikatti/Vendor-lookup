def classify(score):
    if score >= 90:
        return "AUTO_MATCH"
    elif score >= 75:
        return "SUGGESTED"
    return "NO_MATCH"