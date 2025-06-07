# modules/eco_assessment.py

def assess_sustainability(clothing_text):
    # Mock sustainability score logic
    keywords = {
        "organic cotton": 9,
        "recycled polyester": 8,
        "leather": 2,
        "synthetic": 3,
        "hemp": 10,
        "bamboo": 8,
    }
    score = 5  # default
    for word, val in keywords.items():
        if word.lower() in clothing_text.lower():
            score = val
            break

    report = {
        "score": score,
        "verdict": "Highly Sustainable" if score >= 8 else
                   "Moderately Sustainable" if score >= 5 else
                   "Unsustainable",
        "suggestion": "Consider natural or recycled materials for better sustainability."
    }
    return report
