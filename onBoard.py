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
#
import session

cgitb.enable()

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
  print ('Content-type: text/html')
  print()
  print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
  print ('<body>')
  print ('<p style = "color:red">')
  print (err)
  print ('</p>')
  #close the document
  print (results)




  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
  print("<p>Fix your code or Contact the system admin</p></body></html>")
  print ('</body></html>')
  quit()

cursor = conn.cursor() #Create cursor used to run queries



#CGI START

#Coming from signin.html
if form.getvalue("newUser")=="False":
    #Authenticate



    try:
        query = "SELECT Username,Name,Password FROM USERS WHERE Username=%s AND Password=%s;"
        cursor.execute(query,(form.getvalue("Username"),form.getvalue("Password")))
        results = cursor.fetchall()
        if results!=[]:
            # print ('Content-type: text/html')
            # print()
            # print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
            # print ('<body>')
            # print ('<p style = "color:red">')
            # print ("Welcome back")
            # print ('</p>')
            # print ('<p style = "color:red">')
            # print ("SQL worked")
            # print ('</p>')
            print("Location: http://midn.cyber.usna.edu/~m202556/Project/messagePost.py\n")

        else:
            print("Location: http://midn.cyber.usna.edu/~m202556/Project/login.html\n")
    #     #close the document
        print (results)
    except mysql.connector.Error as err:
        print ('<p style = "color:red">')
        print (err)
        print ('</p>')
    #     #close the document

    #Create Message Board


#Coming from signup.html
elif form.getvalue("newUser")=="True":
    #Validate input



    #Insert into Users Table
    try:
        query = "SELECT Username FROM USERS WHERE Username=%s;"
        cursor.execute(query,(form.getvalue("Username"),))
        results = cursor.fetchall()
        if results != []:
            #Username taken
            print("Location: http://midn.cyber.usna.edu/~m202556/Project/signup.html\n")

        else:
            query = "Insert into USERS(Username,Name,Password) values (%s,%s,%s)"
            cursor.execute(query,(form.getvalue("Username"),form.getvalue("Name"),form.getvalue("Password")))
            print ('Content-type: text/html')
            print()
            print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
            print ('<body>')
            print ('<p style = "color:red">')
            print ("hello newbie")
            print ('</p>')
            print ('<p style = "color:red">')
            print('inserted into database (hopefully)')
            print('</p>')
            cursor.close() # close cursor when no longer needed to access database

            conn.commit() # commit the transaction, all changes will be lost if this line is not run!

            conn.close()





    #     print ('</body></html>')
    except mysql.connector.Error as err:
        print ('Content-type: text/html')
        print()
        print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
        print ('<body>')
        print ('<p style = "color:red">')
        print (err)
        print ('</p>')
    #     #close the document
    #     #Create Message Board

else:
      print("Location: http://midn.cyber.usna.edu/~m202556/Project/login.html\n")

print ('</body></html>')
