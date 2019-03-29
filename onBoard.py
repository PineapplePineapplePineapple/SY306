#!/usr/bin/env python3

#onBoard.py
#processes credentials from signup/login page

#Modules
import cgi
import cgitb
import re
#SQL Modules
import mysql.connector #library for database being used
from mysql.connector import errorcode #  allows error handling
import config

# userRegex=re.compile('\d+')
# nameRegex=re.compile('\d+')
passwordRegex=re.compile('\d+')

#Form utilities
form = cgi.FieldStorage()
#SQL connection
try:
    conn = mysql.connector.connect(user=config.USER,
                                  password = config.PASSWORD,
                                  host = config.HOST,
                                  database=config.DATABASE)

except mysql.connector.Error as err:
  #If we have an error connecting to the database we would like to output this fact.
  #This requires that we output the HTTP headers and some HTML.
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
  print("<p>Fix your code or Contact the system admin</p></body></html>")
  quit()

cursor = conn.cursor() #Create cursor used to run queries




if form["newUser"]==False:
    #Authenticate
    #Create Message Board

elif form["newUser"]==True:
    #Validate input
    #Insert into Users Table
    query = "Insert into USERS(Username,Name,Password,Role) values ('" + form(Username) + "','" + form(Name) + "','" + form(Password) + "')"
    try:
      cursor.execute(query)
    except mysql.connector.Error as err:
      #for DEBUG only we'll print the error - we should print some generic message instead for production site

      #If we are going to debug, we need to declare the HTTP Headers and html then exit
      print ('Content-type: text/html')
      print()
      print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
      print ('<body>')
      print ('<p style = "color:red">')
      print (err)
      print ('</p>')
      #close the document
      print ('</body></html>')

    #Create Message Board
