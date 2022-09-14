-- Forward engineer the dojos_and_ninjas_schema from the previous chapter

-- Create a .txt file where you'll save each of your queries from below

-- Query: Create 3 new dojos
Insert into (dojos_and_ninjas_schema)
Values ('Las Vegas'),('Burbank'),('Seattle');


-- Query: Delete the 3 dojos you just created
Delete From (dojos_and_ninjas_schema.dojos) Where dojo.id<= 3;

-- Query: Create 3 more dojos
Insert into (dojos_and_ninjas_schema)
Values ('Las Vegas'), ('Burbank'),('Seattle');

-- Query: Create 3 ninjas that belong to the first dojo
Insert into ninjas (first_name, last_name, age, dojo_id)
Values ('Mike', 'Micky', '22','4'),('Pike', 'Picky','23','4'),('Spike','Spikey','24','4');

-- Query: Create 3 ninjas that belong to the second dojo
Insert into ninjas (first_name, last_name, age, dojo_id)
Values ('Mike', 'Micky', '22','5'),('Pike', 'Picky','23','5'),('Spike','Spikey','24','5');

-- Query: Create 3 ninjas that belong to the third dojo
Insert into ninjas (first_name, last_name, age, dojo_id)
Values ('Mike', 'Micky', '22','6'),('Pike', 'Picky','23','6'),('Spike','Spikey','24','6');

-- Query: Retrieve all the ninjas from the first dojo
Select * From dojos where id = (Select ninjas From dojos order by id Desc Limit 4)
-- Query: Retrieve all the ninjas from the last dojo
Select * From dojos where id = (Select ninja From dojos order by id Desc Limit 6);

-- Query: Retrieve the last ninja's dojo
SELECT * FROM dojos WHERE id = (SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 6);


-- Submit your .txt file that contains all the queries you ran in the shell