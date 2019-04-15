#!/usr/bin/env python3

# messagePost.py
# This file creates the dynamic message board, allows us to add messsages to sql database, print messages dynamically
# onto the message board, and delete the messages that the user has posted
# Kestrel Kuhne

import cgi,cgitb
import time

cgitb.enable()

import mysql.connector
from mysql.connector import errorcode

import config
import session

try:
  conn = mysql.connector.connect(user=config.USER,
                                password = config.PASSWORD,
                                host = config.HOST,
                                database=config.DATABASE)

except mysql.connector.Error as err:
  #If we have an error connecting to the database we would like to output this fact.
  #This requires that we output the HTTP headers and some HTML.
  print ( "Content-type: text/html" )
  print()
  print ("""\
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset = "utf-8">
  <title>DB connection with Python</title>
  <style type = "text/css">
  table, td, th {border:1px solid black}
  </style>
  </head>
  <body>
  """)
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
  print("<p>Fix your code or Contact the system admin</p></body></html>")
  quit()



def addMessage(cursor, content, username):

  #create query statement
  query = "Insert into MESSAGES(Username, Content) values (%s,%s)"
  #execute the query
  try:
    cursor.execute(query,(username,content))
  except mysql.connector.Error as err:

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

  #check number of rows affected > 0 if insert successful
  nbRowsInserted = cursor.rowcount
  songID = cursor.lastrowid

  if nbRowsInserted > 0:

    return 1
  else:
    ##return False
    return 0



def printMessage(cursor):
  query = "SELECT MESSAGES.Username, Content, Time, MID FROM USERS, MESSAGES WHERE USERS.Username = MESSAGES.Username ORDER BY Time"
  try:
    cursor.execute(query)
  except mysql.connector.Error as err:
    #for DEBUG only we'll print the error and statement- we should print some generic message instead for production site
    print ('<p style = "color:red">')
    print(err)
    print (" for statement" + cursor.statement )
    print ('</p>')

  nbRows = 0

  newmessages="<ul class=\"collection with-header\">"
  for (Username, Content, Time, MID) in cursor:
     if Username==currentSession["Username"] or currentSession["Role"]=="admin":
         newmessages += "<li class=\"collection-item\"><div>"+ str(Username)+"<br>"+str(Content)+"<br>"+str(Time)+ "<a href=\"messagePost.py?del="+str(MID)+"\" class=\"secondary-content\"><i class=\"material-icons\">delete</i></a></div></li>\n"
     else:
         newmessages += "<li class=\"collection-item\"><div>"+ str(Username)+"<br>"+str(Content)+"<br>"+str(Time)+ "</div></li>\n"


     nbRows+=1

  if nbRows > 0:
    return newmessages + "</ul>"
  else:
    return ""




#create cursor to send queries
cursor = conn.cursor()
#Begin session
currentSession=session.start()
username = currentSession["Username"]

#see if needed to insert data - get parameters from the form
params = cgi.FieldStorage()
talk = params.getvalue("talk")
#see if deletion request was made
delete= params.getvalue("del")

#if insert button was pushed
if talk:

  content = params.getvalue("talk")
  result = addMessage(cursor, content, username)
  #print either a confirmation message or error message
  # if result==1:
  #
  #   #print('Status: 303 See Other')
  print('Location: messagePost.py')

if delete:
    query = "SELECT MESSAGES.Username FROM MESSAGES WHERE MID="+str(delete)
    try:
       cursor.execute(query)
    except mysql.connector.Error as err:
        print ('Content-type: text/html')
        print()
        print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
        print ('<body>')
        print ('<p style = "color:red">')
        print (err)
        print ('</p>')
        #close the document
        print ('</body></html>')
    for (Username,) in cursor:
        if Username==currentSession["Username"] or currentSession["Role"]=="admin":
            query = "DELETE FROM MESSAGES where MID="+str(delete)
        #   #execute the query
            try:
               cursor.execute(query)
            except mysql.connector.Error as err:
                print ('Content-type: text/html')
                print()
                print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
                print ('<body>')
                print ('<p style = "color:red">')
                print (err)
                print ('</p>')
                #close the document
                print ('</body></html>')




#First we need our HTTP headers and HTML opening code
print ( "Content-type: text/html" )
print()
print ("""\
<!DOCTYPE html>
<html>
<head>
  <meta charset = "utf-8">
  <title>ACME Board</title>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link rel="icon" href="http://static1.squarespace.com/static/537ffea2e4b011aa8abe92c9/t/550ae1f8e4b01e598aec20dc/1548191522912/">
  <link rel="stylesheet" type="text/css" href="acme.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

</head>
<body>

<nav class="black">
<div class="nav-wrapper container">
  <a href="#" class="brand-logo">ACME</a>
  <ul id="nav-mobile" class="right hide-on-med-and-down">
    <li><a href="login.html">Change user</a></li>
    <li>""" + username + """</li>
  </ul>
</div>
</nav>


<div class="body">
<div class="container z-depth-3">

</p>
<br>
<table class="col s6 offset-s3">
	<tr>
		<td>
""")

print ("""\
    <form action="messagePost.py" method="post">
    <p>
        <textarea id ="ta" rows="10" cols="120" name="talk"></textarea> <br />
<label for="ta">Talk anything and everything... </label>
<button class="btn waves-effect waves-light #c62828 red darken-3" type="submit" name="insert" style="display: block; margin: 0 auto;">Talk
<i class="material-icons right">record_voice_over</i>
</button>
    </p>
</form>
""")


message = printMessage(cursor)

if message:
  print (message)
else:
  print ("<h2>No messages yet!</h2>")

#close cursor since we don't use it anymore
cursor.close()

#commit the transaction
conn.commit()  #this is really important otherwise all changes lost

#close connection
conn.close()

#print end html tags
print("""\
</td>
</tr>
</table></div></div>
</body>
</html>
""");
