from flask import Flask, render_template, request, redirect
from model import predict_url
from database import *
import re

app = Flask(__name__)
init_db()

# Dashboard Data
total_scans = 0
safe_scans = 0
phishing_scans = 0

# Scan History
history = []




@app.route("/password_checker", methods=["GET", "POST"])
def password_checker():

    score = 0
    suggestion = ""

    if request.method == "POST":

        password = request.form.get("password", "")

        conditions = [
            len(password) >= 8,
            len(password) <= 12,
            re.search(r"[A-Z]", password),
            re.search(r"[a-z]", password),
            re.search(r"[0-9]", password),
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password),
            password.lower() not in ["password", "123456", "admin", "qwerty"],
            not re.search(r"\d{4}", password)
        ]

        passed = sum(bool(x) for x in conditions)
        score = int((passed / len(conditions)) * 100)

        if score >= 80:
            suggestion = "Excellent! Your password is very strong."
        elif score >= 50:
            suggestion = "Good password. Improve a few conditions."
        else:
            suggestion = "Weak password. Follow all password tips."

    return render_template(
        "password_checker.html",
        score=score,
        suggestion=suggestion
    )

@app.route("/")
def home():

    


    history = get_history()

    total, safe, phishing = get_counts()

    return render_template(
        "index.html",
        history=history,
        total_scans=total,
        safe_scans=safe,
        phishing_scans=phishing
    )



@app.route("/predict", methods=["POST"])
def predict():

    
    global total_scans
    global safe_scans
    global phishing_scans
    global history

    url = request.form.get("url", "").strip()

    if url == "":
        return render_template(
            "index.html",
            total_scans=total_scans,
            safe_scans=safe_scans,
            phishing_scans=phishing_scans,
            history=history[::-1]
        )

    result, score = predict_url(url)

    total_scans += 1

    if "Safe" in result:
        safe_scans += 1
    else:
        phishing_scans += 1

    add_scan(url, result, score)

    history = get_history()

    return render_template(
        "result.html",
        url=url,
        result=result,
        score=score
    )


@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        total_scans=total_scans,
        safe_scans=safe_scans,
        phishing_scans=phishing_scans
    )


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/url_scanner")
def url_scanner():
    history = get_history()
    total, safe, phishing = get_counts()

    return render_template(
        "index.html",
        history=history,
        total_scans=total,
        safe_scans=safe,
        phishing_scans=phishing
    )


if __name__ == "__main__":
    app.run(debug=True)