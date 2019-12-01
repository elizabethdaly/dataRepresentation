# week 09 Lab 09.02
#
# pip install mysql-connector-python
# NOT
# pip install mysql-connector
# https://stackoverflow.com/questions/34168651/what-are-the-differences-between-mysql-connector-python-mysql-connector-python

import mysql.connector
#print("imported")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "datarepresentation"
)

mycursor = mydb.cursor()
sql = "insert into student (name, age) values (%s, %s)"
values = ("John", 52)
mycursor.execute(sql, values)

mydb.commit()
print("1 record inserted, ID: ", mycursor.lastrowid)