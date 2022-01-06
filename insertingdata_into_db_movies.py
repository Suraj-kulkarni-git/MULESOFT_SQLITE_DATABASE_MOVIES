import sqlite3

#connecting to the existing database
conn = sqlite3.connect('movies.db')


cursor = conn.cursor()

#inserting the data in the table movies
cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Singham', 'Ajay Devgn', 'Kajal Aggarwal ', 2011, 'Rohit Shetty')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('PK', 'Amir Khan', 'Anushka Sharma', 2014, 'Rajkumar Hirani')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Baahubali', 'Prabhas', 'Tamannaah Bhatia', 2015 , 'S. S. Rajamouli')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Dilwale', 'Shah Rukh Khan', 'Kajol', 2015 , 'Rohit Shetty')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Dangal', 'Amir Khan', 'Sakshi Tanwar', 2016, 'Nilesh Tiwari')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Sultan', 'Salman Khan', 'Anushka Sharma', 2016, 'Ali Abbas Zafar')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Raees', 'Shah Rukh Khan', 'Mahira Khan', 2017, 'Rahul Dholakia')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Simmba', 'Ranveer Singh', 'Sara Ali Khan', 2018, 'Rohit Shetty')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('Radhe', 'Salman Khan', 'Disha Patani', 2021, 'Prabhu Deva')''')


conn.commit()
#printing if the datas are successfully inserted
print("Records inserted........")


conn.close()