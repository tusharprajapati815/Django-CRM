#Install Mysql on your computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'MYsTu@#1235'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database

cursorObject.execute("CREATE DATABASE elderorg")

print("ALL DONE!")
