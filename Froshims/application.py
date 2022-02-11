from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Linking database
db = SQL("sqlite:///froshims.db")

# Valid sports for registration
SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Basketball"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    # Validate sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Please choose a sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    # Register registrant
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    return redirect("/registrants")


# List of all the students who registered
@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)
