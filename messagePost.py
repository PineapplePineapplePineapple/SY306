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


# access data from config.py to connect to mysql database
try:
  conn = mysql.connector.connect(user=config.USER,
                                password = config.PASSWORD,
                                host = config.HOST,
                                database=config.DATABASE)

# error checking if the mysql database fails
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
  # error checking continued
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
  print("<p>Fix your code or Contact the system admin</p></body></html>")
  quit()


# addMessage function adds the written messags into the mysql database for the specified user
def addMessage(cursor, content, username):

  #create query statement
  query = "Insert into MESSAGES(Username, Content) values (%s,%s)"
  #execute the query
  try:
    cursor.execute(query,(username,html_escape(content)))
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
    #return True
    return 1
  else:
    ##return False
    return 0


# printMessage function does a SELECT statement and prints out all of the messages on the message board that have been
#entered into the database.
def printMessage(cursor):
#query statement for printing the messages onto the message board and ordering the messages by time
  query = "SELECT MESSAGES.Username, Content, Time, MID FROM USERS, MESSAGES WHERE USERS.Username = MESSAGES.Username ORDER BY Time"
  try:
    #execute query statement
    cursor.execute(query)
  except mysql.connector.Error as err:
    #for DEBUG only we'll print the error and statement- we should print some generic message instead for production site
    print ('<p style = "color:red">')
    print(err)
    print (" for statement" + cursor.statement )
    print ('</p>')

  nbRows = 0

  newmessages="<ul class=\"collection with-header\">"
  # run a for loop for all of the messages in the message table
  for (Username, Content, Time, MID) in cursor:
     # if that specific user wrote that message a delete button appears and they can delete their own messages. Admin can
     # delete all messages
     if Username==currentSession["Username"] or currentSession["Role"]=="admin":
          # a delete button appears if the above parameters in the if statement are met -- we used a variable called del that equals the Message ID if the delete button for that message is clicked on
         newmessages += "<li class=\"red lighten-5 collection-item\"><div>"+ str(Username)+"<p class=\"flow-text\">"+str(Content)+"</p>"+str(Time)+ "<a href=\"messagePost.py?del="+str(MID)+"\" class=\"secondary-content\"><i class=\"material-icons\">delete</i></a></div></li>\n"
     else:
         # if the requirements are not met then no delete button appears
         newmessages += "<li class=\"collection-item\"><div>"+ str(Username)+"<br>"+str(Content)+"<br>"+str(Time)+ "</div></li>\n"


     nbRows+=1

#prints out the rows with all of the messages
  if nbRows > 0:
    return newmessages + "</ul>"
  else:
    return ""




#create cursor to send queries
cursor = conn.cursor()
#Begin session
currentSession=session.start()
# grab the username that is being used in the current session
try:
    username = currentSession["Username"]
except:
    print('Location:signup.html')




#see if needed to insert data - get parameters from the form
params = cgi.FieldStorage()
talk = params.getvalue("talk")
#see if deletion request was made
delete= params.getvalue("del")

#if talk button was pushed
if talk:

  content = params.getvalue("talk")
  # pass the parameteres into addMessage which adds the message info into the database
  result = addMessage(cursor, content, username)
  # reload the message board with the new message added
  print('Location: messagePost.py')

# if the deletion request was made we check to make sure that the deletion request is coming from the user who wrote the message
if delete:
    # query statement to grab the Username making the deletion request
    query = "SELECT MESSAGES.Username FROM MESSAGES WHERE MID="+str(delete)
    try:
    # execute the query
       cursor.execute(query)
    # error checking if query goes wrong
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
    # for loop for the Username being called
    for (Username,) in cursor:
        # if the Username matches the current session username or the admin account is being used then delete the message from the database
        if Username==currentSession["Username"] or currentSession["Role"]=="admin":
            query = "DELETE FROM MESSAGES where MID="+str(delete)
        #   #execute the query
            try:
               cursor.execute(query)
            # error checking
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
# the HTML format for our message board -- normal styling w/ the ability to sign out in the top right corner by clicking on your username
# we name the textarea part of the message board "talk" so that when the user writes a message talk=True and we can
# run that check to print the messages to the message board
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
    <li><a href="login.html">Logged in as: <b>""" + username + """</b></a></li>
  </ul>
</div>
</nav>


<div class="body">
<div class="container z-depth-3">


<table class="col s6 offset-s3">
	<tr>
		<td>
""")

print ("""\
  <div class="row">
    <form action="messagePost.py" method="post" class="col s8 offset-s2">
      <div class="row">
        <div class="input-field col s8">
          <textarea id="ta" name="talk" class="materialize-textarea" data-length="5000"></textarea>
        </div>
        <button class="btn-floating waves-effect waves-light #c62828 red darken-3" type="submit" name="insert" style="display: block; margin: 0 auto;">
        <i class="material-icons right">record_voice_over</i>
        </button>
      </div>
    </form>
  </div>
</form>
""")

#calling the printMessage function when the message board is logged into so that all messages appear
message = printMessage(cursor)

# if messages exist print them out, if not then show 'No messages yet'
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
