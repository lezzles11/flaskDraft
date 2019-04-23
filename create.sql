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
