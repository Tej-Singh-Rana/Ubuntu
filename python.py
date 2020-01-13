#!/usr/bin/python3

import cgi, cgitb
import os

#mysql database connectivity

import mysql.connector

mydb = mysql.connector.connect(
  host="web1",
  user="root",
  passwd="redhat123",
  database="users"
)

mycursor = mydb.cursor()
mycursor.execute("select * from login")
myresult = mycursor.fetchall() # it gives the list

# Create instance of FieldStorage
print ("Content-Type: text/html\n")

form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('Username')
password  = form.getvalue('Password')


for row in myresult:
        if (username == row[0]) and (password == row[1]):
                print("Content-Type: text/html\n")
                print("welcome")

        else:
                print("Content-Type: text/html\n")
                print("<h2>Username and Password Incorrect</h2>")


mycursor.close()
