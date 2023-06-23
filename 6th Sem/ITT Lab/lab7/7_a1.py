import sqlite3

try:
    connection = sqlite3.connect('test.db')
    print("Opened Database Successfully")
    cursor = connection.cursor()
    print("Opened Cursor Successfully")
except Exception as e:
    print("Error occured", e)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS validate(
    pnum int PRIMARY KEY NOT NULL,
    email TEXT NOT NULL);
    ''')

login = [
    (1111, "123@gmail.com"),
    (2222, "b@gmail.com"),
    (3333, "that@hotmail.com"),
    (4444, "pot@yahoo.in"),
]

cursor.executemany("INSERT INTO validate VALUES (?, ?)", login)

#for row in cursor.execute("select * from validate"):
#    print(row)

name = int(input("Enter Phone number: "))
print(name)
password = input("Enter email: ")
print(password)

f=0
for row in cursor.execute("select * from validate"):
    if row[0] == name and row[1] == password:
        print("Login Successful")
        f =1
        break
if f==0:
    print("Login Failed")