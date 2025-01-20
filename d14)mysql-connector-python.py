import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Santhosh@123")
mycursor = mydb.cursor()
"""
# show db
mycursor.execute("show databases")
# print(mycursor)
for i in mycursor:
    print(i)
"""
"""
# create db
mycursor.execute("create database santhosh")
"""

# create table in db
# mydb = mysql.connector.connect(host="localhost", user="root", password="Santhosh@123", database="santhosh")
# mycursor = mydb.cursor()
# mycursor.execute("create table star(name VARCHAR(290), address VARCHAR(50))")
# mydb.commit()

"""
# insert value in table
# x = "insert into star values('Ram', 'Trichy')"
x = "insert into star values(%s, %s)"
y = ('Ram','Trichy')
mycursor.execute(x,y)
mydb.commit()
"""
"""
# insert multiple values in table
x = "insert into star(name,address) values(%s,%s)"
y = [('Tamil','Chennai'),('Kaali','Madurai'),('Askhaya','Coimbatore')]
# mycursor.execute(x, y)
mycursor.executemany(x, y)
mydb.commit()
"""
"""
# drop table/drop database(commit() is not needed)
mycursor.execute("drop table star")
mycursor.execute("drop database santhosh")
mydb.commit()
"""
"""
mycursor.execute("create database school")
mycursor.execute("use school")
mycursor.execute("create table students(name varchar(255), address varchar(255), age int)")
y = "insert into students(name,address,age) values(%s,%s,%s)"
x = [('Tamil','Chennai',18),('Kaali','Madurai',13),('Askhaya','Coimbatore',16)]
mycursor.executemany(y,x)
mydb.commit()
"""
