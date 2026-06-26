import re

def predict_url(url):

    score = 100

    url = url.lower()

    # -----------------------------------
    # HTTPS Check
    # -----------------------------------

    if url.startswith("https://"):
        score += 5
    else:
        score -= 25

    # -----------------------------------
    # HTTP Check
    # -----------------------------------

    if url.startswith("http://"):
        score -= 20

    # -----------------------------------
    # IP Address Detection
    # -----------------------------------

    ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"

    if re.search(ip_pattern, url):
        score -= 30

    # -----------------------------------
    # @ Symbol
    # -----------------------------------

    if "@" in url:
        score -= 25

    # -----------------------------------
    # Too Many Dots
    # -----------------------------------

    if url.count(".") > 3:
        score -= 15

    # -----------------------------------
    # Long URL
    # -----------------------------------

    if len(url) > 75:
        score -= 15

    # -----------------------------------
    # Suspicious Keywords
    # -----------------------------------

    keywords = [

        "login",
        "signin",
        "verify",
        "update",
        "secure",
        "account",
        "bank",
        "paypal",
        "wallet",
        "bonus",
        "gift",
        "free",
        "confirm",
        "otp",
        "password",
        "recover",
        "security"

    ]

    for word in keywords:

        if word in url:
            score -= 8

    # -----------------------------------
    # Shortened URLs
    # -----------------------------------

    shorteners = [

        "bit.ly",
        "tinyurl",
        "goo.gl",
        "t.co",
        "rb.gy",
        "is.gd"

    ]

    for short in shorteners:

        if short in url:
            score -= 25

    # -----------------------------------
    # Trusted Domains
    # -----------------------------------

    trusted = [

        "google.com",
        "youtube.com",
        "github.com",
        "microsoft.com",
        "apple.com",
        "amazon.in",
        "amazon.com",
        "wikipedia.org",
        "openai.com"

    ]

    for site in trusted:

        if site in url:
            score = max(score, 90)

    # -----------------------------------

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    # -----------------------------------

    if score >= 80:

        result = "✅ Safe Website"

    elif score >= 50:

        result = "⚠ Suspicious Website"

    else:

        result = "❌ Phishing Website"

    return result, score