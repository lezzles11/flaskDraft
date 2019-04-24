import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)
#only accepts post requests 
@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    #TRY - possibility that something that could wrong 
    #handle the error. TRY take the request flight id - and try to convert to integer 
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
    	#RETURNING 404 
        return render_template("404.html", message="Invalid flight number.")

    # Make sure flight exists.
    #RUNNING SQL QUERY HERE - PLUG IN ID - rowcount - how many rows did you get back? IF THERE WAS
    #NO MATCHING ROLES, "no such flight with that id."
    """0 ROWS HAD AN IDEA"""
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id.")
    """Run that insert query - hook them in the table (run db.execute) - 
    INSERT THEM AND THEIR VALUE
    THIS IS THE COOLEST THING EVER!!
    """
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
            {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    """Lists all flights."""
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

#<INT:FLIGHT_ID> IS JUST A PLACEHOLDER! int - could be substituted for any integer 
@app.route("/flights/<int:flight_id>")
#FLIGHT_ID PARAMETER. take to flight function - so in URL you need to specify what you care about 
def flight(flight_id):
    """Lists details about a single flight."""

    # Make sure flight exists.
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # Get all passengers.
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)
