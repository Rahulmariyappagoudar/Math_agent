def check_hitl(parsed, verification):

    if "Confidence: High" in verification:
        return "AUTO_APPROVED"

    if "Confidence: Medium" in verification:
        return "REVIEW_RECOMMENDED"

    return "HUMAN_REQUIRED"