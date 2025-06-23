def get_risk_thresholds():
    return {
        "low": 0.5,
        "medium": 0.75,
        "high": 0.9,
    }

def categorize_risk(prob, thresholds=None):
    thresholds = thresholds or get_risk_thresholds()
    if prob < thresholds["low"]:
        return "Low"
    elif prob < thresholds["medium"]:
        return "Medium"
    elif prob < thresholds["high"]:
        return "High"
    else:
        return "Critical"