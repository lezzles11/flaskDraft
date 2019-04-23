#Create table and name it glasses
CREATE TABLE glasses (
	#What types of information it will contain 
	#ID -> common keyword. (refernce each pair. )
	#PRIMARY KEY = primary way i'm going to reference this
	#SERIAL -> automatically count up 
	id SERIAL PRIMARY KEY, 
	#defining other columns 
	#not null - doesn't need a value, but can have 
	origin VARCHAR NOT NULL, 
	#if it is null, it will reject it 
	destination VARCHAR NOT NULL, 
	quantity INTEGER NOT NUll
);


CREATE TABLE glasses (
	id SERIAL PRIMARY KEY, 
	origin VARCHAR NOT NULL, 
	destination VARCHAR NOT NULL, 
	quantity INTEGER NOT NUll
);

#how to insert values in database
INSERT INTO glasses (origin, destination, quantity) VALUES ('Bangladesh', 'Hong Kong', 1);

#looking at values 
SELECT * FROM glasses; 

#looking only at certain columns 
SELECT origin, destination FROM glasses;

#looking at only at certain rows 
SELECT * FROM glasses WHERE id = 3;
SELECT * FROM glasses WHERE origin = 'Hong Kong';
SELECT * FROM glasses WHERE quantity > 5 OR origin = 'Hong Kong';

#looking for specifics (look for all with letter 'a')
SELECT * FROM glasses WHERE origin LIKE '%a%';

#changing data - WHERE SPECIFIES ABOUT WHERE YOU ARE MODIFYING IT 
UPDATE glasses
	SET quantity = 300
	#ONLY CHANGE FOR NEW YORK ANd DESTINATION HONG KONG
	WHERE origin = 'New York'
	AND destination = 'London';

#deleting row of data 
DELETE FROM glasses 
	WHERE origin = "Hong Kong";

#ordering the data
SELECT * FROM glasses ORDER BY quantity ASC;

#ordering the data getting only the lowest three
SELECT * FROM glasses ORDER BY quantity ASC LIMIT 3;

#grouping data and counting how many you have from each 
SELECT origin, COUNT(*) FROM glasses GROUP BY origin; 

#grouping data and counting the ones that only have greater than one
SELECT origin, COUNT(*) FROM glasses GROUP BY origin HAVING COUNT(*) > 1;

#creating clients that USE the data glasses
CREATE TABLE clients (
	id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL, 
	glasses_id INTEGER REFERENCES glasses
	);

#joining TWO tables!! make sure you tell the relationship via ON 
SELECT origin, destination, name FROM glasses JOIN clients ON
#if you take the passengers and get the flight id column, that should match the id column via flights
passengers.flight_id = flights.id 
#IDEAS = 

#printing out the name and all the details 
SELECT origin, destination, name FROM glasses JOIN clients ON
#if you take the passengers and get the flight id column, that should match the id column via flights
clients.glasses_id = glasses.id WHERE name = 'Alice';


#forcing joins (so it prints out both tables, even if the headers dont match)
#printing out the name and all the details 
#LEFTJOIN; OR RIGHTJOIN (print out all the tables from the LEFT (Glasses) or RIGHT (clients))
SELECT origin, destination, name FROM glasses LEFT JOIN clients ON
#if you take the passengers and get the flight id column, that should match the id column via flights
clients.glasses_id = glasses.id;


#TYPES OF JOINS
#JOIN/INNER JOIN; LEFT OUTER JOIN; RIGHT OUTER JOIN; FULL OUTER JOIN 

#INDEXES - easy way to reference to something else 
#if i'm going to be referencing origin A LOT, it might helpful to index my origins 
#but it SLOWS THINGS DOWN, so only index if you use it a lot 
#also takes space


#combining to make it easier to find stuff 
#in the table glasses, select all clients that have greateer than one 
SELECT * FROM glasses where id in 
#grouping the data and counting the ones that only have greater than one 
(SELECT glasses_id FROM clients
GROUP BY glasses_id HAVING COUNT (*) > 1)







































