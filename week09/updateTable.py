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
sql = "update student set name = %s, age = %s where id = %s"
values = ("Joe", 33, 1)
mycursor.execute(sql, values)

mydb.commit()
print("update done")