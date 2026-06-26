from flask import Flask, render_template, request, redirect
from model import predict_url
from database import *

app = Flask(__name__)
init_db()

# Dashboard Data
total_scans = 0
safe_scans = 0
phishing_scans = 0

# Scan History
history = []


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


@app.route("/password_checker")
def password_checker():
    return render_template(
        "password_checker.html",
        score=0,
        suggestion="Enter Password"
    )


@app.route("/url_scanner")
def url_scanner():

    return render_template(
        "index.html",
        total_scans=total_scans,
        safe_scans=safe_scans,
        phishing_scans=phishing_scans,
        history=history[::-1]
    )


if __name__ == "__main__":
    app.run(debug=True)