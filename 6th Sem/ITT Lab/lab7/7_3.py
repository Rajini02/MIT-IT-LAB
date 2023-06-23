import sqlite3

try:
    connection = sqlite3.connect('test.db')
    print("Opened Database Successfully")
    cursor = connection.cursor()
    print("Opened Cursor Successfully")
except Exception as e:
    print("Error occured", e)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT(
    REGNO INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    DEPARTMENT TEXT NOT NULL);
    ''')

students = [
    (180911168, "A", 20, "IT"),
    (180932156, "B", 20, "CSE"),
    (180911169, "C", 20, "CHEM"),
    (180911170, "D", 20, "IT"),
]

cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", students)

query_term = int(input("\nEnter the registration number of student to search for: "))
print("Query Output:")
for row in cursor.execute("SELECT * FROM STUDENT WHERE REGNO = (?)", (query_term,)):
    print(row)