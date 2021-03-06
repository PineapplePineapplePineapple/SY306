#!/usr/bin/env python3

#onBoard.py
#processes credentials from signup/login page and directs users to the message board if they Authenticate
#maintainer: Jacques Henot

#Modules
import cgi
import cgitb
import re
import hashlib
#SQL Modules
import mysql.connector #library for database being used
from mysql.connector import errorcode #  allows error handling
import config
#Session Modules
import session

cgitb.enable()

passwordRegex=re.compile('\d+')

#Form utilities
form = cgi.FieldStorage()
#Session Dictionary to be used
SDict=session.start()

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
}
#Taken from https://wiki.python.org/moin/EscapingHtml
def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)







#SQL connection
try:
    conn = mysql.connector.connect(user=config.USER,
                                  password = config.PASSWORD,
                                  host = config.HOST,
                                  database=config.DATABASE)

except mysql.connector.Error as err:
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


if (form.getvalue("Username")==None):
    print("Location: http://midn.cyber.usna.edu/~m202556/project03/login.html\n")
if (form.getvalue("Password")==None):
    print("Location: http://midn.cyber.usna.edu/~m202556/project03/login.html\n")


#CGI START

#Coming from signin.html###############################################################
if form.getvalue("newUser")=="False":
    #Authenticate
    try:
        query = "SELECT Username,Name,Password,Role FROM USERS WHERE Username=%s AND Password=%s;"
        pDigest=hashlib.sha256((form.getvalue("Password")+form.getvalue("Username")).encode("utf-8")).hexdigest()
        cursor.execute(query,(form.getvalue("Username"),pDigest))
        results = cursor.fetchall()

        #Successful login flow
        if results!=[]:
            #Creates session
            SDict["Username"]=results[0][0]
            SDict["Role"]=results[0][3]
            session.end(SDict)
            #Direct user to the message board
            if results[0][3]=="admin":
                print("Location: http://midn.cyber.usna.edu/~m202556/project03/admin/admin.html\n")
            else:
                print("Location: http://midn.cyber.usna.edu/~m202556/project03/messagePost.py\n")

        #Failed login flow
        else:

            session.end(SDict)
            #refreshed the login page, and triggers the 'invalid credentials' error message
            print("Location: http://midn.cyber.usna.edu/~m202556/project03/login.html\n")

    except mysql.connector.Error as err:
        print ('<p style = "color:red">')
        print (err)
        print ('</p>')
################################################################################################


#Coming from signup.html########################################################################
elif form.getvalue("newUser")=="True":

    #Insert into Users Table
    try:
        query = "SELECT Username FROM USERS WHERE Username=%s;"
        cursor.execute(query,(form.getvalue("Username"),))
        results = cursor.fetchall()

        #Verify no existing user with the same Username exists
        if results != []:
            #Username taken
            session.end(SDict)
            print("Location: http://midn.cyber.usna.edu/~m202556/project03/signup.html\n")

        #Create user if no such prexisting user exists
        else:
            query = "Insert into USERS(Username,Name,Password) values (%s,%s,%s)"

            pDigest=hashlib.sha256((form.getvalue("Password")+form.getvalue("Username")).encode("utf-8")).hexdigest()
            cursor.execute(query,(html_escape(form.getvalue("Username")),html_escape(form.getvalue("Name")),pDigest))
            #Direct the user to login
            print("Location: http://midn.cyber.usna.edu/~m202556/project03/login.html\n")

            cursor.close() # close cursor when no longer needed to access database

            conn.commit() # commit the transaction

            conn.close()





    except mysql.connector.Error as err:
        print ('Content-type: text/html')
        print()
        print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
        print ('<body>')
        print ('<p style = "color:red">')
        print (err)
        print ('</p>')
######################################################################################################



#Access CGI directly###################################################################################
else:
      session.end(SDict)
      print("Location: http://midn.cyber.usna.edu/~m202556/project03/login.html\n")

print ('</body></html>')
#######################################################################################################
