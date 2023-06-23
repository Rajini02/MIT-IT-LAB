import sqlite3

try:
    connection = sqlite3.connect('test.db')
    print("Opened Database Successfully")
    cursor = connection.cursor()
    print("Opened Cursor Successfully")
except Exception as e:
    print("Error occured", e)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS logins(
    uname text PRIMARY KEY NOT NULL,
    pass TEXT NOT NULL);
    ''')

login = [
    ("abc", "123"),
    ("def", "B"),
    ("ghi", "C"),
    ("jkl", "D"),
]

cursor.executemany("INSERT INTO logins VALUES (?, ?)", login)
f=0
name = input("Enter username: ")
password = input("Enter password: ")
for row in cursor.execute("select * from logins"):
    if row[0] == name and row[1] == password:
        print("Login Successful")
        f =1
        break
if f==0:
    print("Login Failed")