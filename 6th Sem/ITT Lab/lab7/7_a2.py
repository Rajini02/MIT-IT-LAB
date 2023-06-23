import sqlite3

conn = sqlite3.connect('results.db')

cursor = conn.cursor()

#cursor.execute('''CREATE TABLE RESULTS
#                (ID INT PRIMARY KEY NOT NULL,
#                NAME TEXT NOT NULL,
 #               MATHS INT NOT NULL,
  #              SCIENCE INT NOT NULL,
   #             ENGLISH INT NOT NULL,
    #            SOCIAL_STUDIES INT NOT NULL,
     #           COMPUTER_SCIENCE INT NOT NULL);''')

marks = [(1, "Shreeyanka", 70, 80, 85, 75, 90),
         (2, "Ravi", 80, 75, 90, 85, 70),
         (3, "Vidushi", 90, 85, 70, 80, 75),
         ]

cursor.executemany("INSERT INTO RESULTS VALUES (?, ?, ?, ?, ?, ?, ?)", marks)

name = input("Enter the name of the student: ")


for row in cursor.execute("SELECT * FROM RESULTS WHERE NAME=(?)",(name,)):
    result = row



if result:

    total_marks = result[2] + result[3] + result[4] + result[5] + result[6]
    print(f"Total marks obtained by {result[1]}: {total_marks}")
    percentage = total_marks / 5
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    else:
        grade = 'F'

    print(f"Grade obtained by {result[1]}: {grade}")
else:
    print(f"No results found for {name}")