
from flask import Flask, render_template, request, redirect, url_for, session
from database import init_db
from models import create_user, get_user_by_email

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../static",
    static_url_path="/static"
)

# Secret key for session management
app.secret_key = "farmers-platform-local-secret-key"

# Initialize database
init_db()


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not name or not email or not password:
            return "Please fill in all fields."

        try:
            create_user(name, email, password)
            return redirect(url_for("login"))
        except Exception as error:
            print("Registration error:", error)
            return "Registration failed. This email may already be registered."

    return render_template("register.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        user = get_user_by_email(email)

        if user is not None and user["password"] == password:
            session["user_email"] = email
            return redirect(url_for("dashboard"))

        return "Invalid email or password."

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user_email" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# Crop Recommendation
@app.route("/crop-recommendation")
def crop_recommendation():
    return render_template("crop_recommendation.html")


# Weather Information
@app.route("/weather")
def weather():
    return render_template("weather.html")


# Disease Detection
@app.route("/disease-detection")
def disease_detection():
    return render_template("disease_detection.html")


# Fertilizer Guidance
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


# Run Application
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
