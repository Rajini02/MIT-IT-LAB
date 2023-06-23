import sqlite3

try:
    conn = sqlite3.connect('test.db')
    print("Connected to sqlite3")
    cursor = conn.cursor()
    print("Opened Cursor")
except Exception as e:
    print("Failed to open",e)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS GRADES(
    REGNO INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    CG REAL NOT NULL,
    DEPARTMENT TEXT NOT NULL);
    ''')

students = [
    (180911168, "A", 5.7, "IT"),
    (180932134, "B", 8.9, "CSE"),
    (180911169, "C", 7.7, "CHEM"),
    (180911170, "D", 7.8, "IT"),
]

cursor.executemany("insert into grades values (?,?,?,?)", students)

regno = int(input("Enter regno: "))
cgpa = float(input("Enter cgpa: "))

print("Before update")


for row in cursor.execute("SELECT * FROM grades WHERE regno = (?)", (regno,)):
   print(row)

print("After update")

conn.execute("Update grades SET cg = (?) where regno = (?);",(cgpa, regno,))

for row in cursor.execute("SELECT * FROM grades where regno = (?)", (regno,)):
    print(row)
