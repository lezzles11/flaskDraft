#reading data 
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
	#opening the file 
    f = open("flights.csv")
    #python has csv built in 
    reader = csv.reader(f)
    #colon - :origin (placeholder)
    #{} = PROVIDING python dictionary (tells query what to fill in!) so in the origin place holder, fill in origin 
    #can also do for o, des, dur (THOSE ARE ONLY VARIABLES)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()

if __name__ == "__main__":
    main()

