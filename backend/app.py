from flask import Flask, render_template, request, redirect, url_for
from database import init_db
from models import create_user, get_user_by_email

app = Flask(__name__, template_folder="../frontend")


# Initialize database
init_db()


# Home
@app.route("/")
def home():
    return render_template("index.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if name and email and password:
            try:
                create_user(name, email, password)
                return redirect(url_for("login"))
            except Exception:
                return "Email already registered."

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = get_user_by_email(email)

        if user and user["password"] == password:
            return redirect(url_for("dashboard"))

        return "Invalid email or password."

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Crop Recommendation
@app.route("/crop-recommendation")
def crop_recommendation():
    return render_template("crop_recommendation.html")


# Weather
@app.route("/weather")
def weather():
    return render_template("weather.html")


# Disease Detection
@app.route("/disease-detection")
def disease_detection():
    return render_template("disease_detection.html")


# Fertilizer
@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")


# Market Prices
@app.route("/market-prices")
def market_prices():
    return render_template("market_prices.html")


# Farming Guidance
@app.route("/farming-guidance")
def farming_guidance():
    return render_template("farming_guidance.html")


if __name__ == "__main__":
    app.run(debug=True)
    