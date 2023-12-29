#coding: cp1252
import sqlite3

conn=sqlite3.connect("employee.db")
cur=conn.cursor()

print("Database opend successfully")

cur.execute("create table Employees(ID integer primary key AUTOINCREMENT,name text NOT NULL ,age integer NOT NULL,email UNIQUE NOT NULL,address TEXT NOT NULL,contact text NOT NULL)")

print("Table created successfully")


cur.execute("insert into Employees(name,age,email,address,contact) values (?,?,?,?,?)",
                        ("rashmi","30","rashmi@gamil.com","pune,wakad","1234567890"))

conn.commit()

cur.execute("select * from Employees")  
rows = cur.fetchall()
print(rows)


name="rashmi"   
cur.execute("select * from Employees where name='"+ name+"'")
rows=cur.fetchall()
print(rows)
