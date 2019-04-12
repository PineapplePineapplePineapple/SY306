#!/usr/bin/env python3
import cgi,cgitb
import time
from message import message

cgitb.enable()

import mysql.connector
from mysql.connector import errorcode

import config

try:
  conn = mysql.connector.connect(user=config.USER,
                                password = config.PASSWORD,
                                host = config.HOST,
                                database=config.DATABASE)

now = time.strftime('%Y-%m-%d %H-%M-%S')

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

#create cursor to send queries
cursor = conn.cursor()

#see if needed to insert data - get parameters from the form
params = cgi.FieldStorage()
insertButton = params.getvalue("insert")

#if insert button was pushed
if insertButton:

  content = params.getvalue("talk")
  result = message.addMessage(cursor, content, now)
  #print either a confirmation message or error message
  if result==1:

    #print('Status: 303 See Other')
    print('Location: messagePost.py')
    print('Content-type: text/html')
    print()
    #Note, we do not stop execution at this point, there is some clean up to do that
    #is common with the action in the else statement so it follows that.
  else:
   #So if we get to this part of the code it means that the insert failed.
   #We need to print HTTP Headers and content.
   print('Content-type: text/html')
   print()
   print ("""\
   <!DOCTYPE html>
   <html>
   <head>
   <meta charset = "utf-8">
   <meta http-equiv="refresh" content="5; url=song.py">
   <title>DB connection Error</title>
   <style type = "text/css">
   table, td, th {border:1px solid black}
   </style>
   </head>
   <body>
   """)
   print ('<h2>Could not insert the song</h2>')
   #Now we branch depending on the error code encountered.
   if result == 0:
      print ('<p>Sorry, something unexpected happened when we tried to add the song to the database. You will be redirected to the song list shortly.</p>')

  #now need to clean up database cursor, etc
  cursor.close()
  #commit the transaction
  conn.commit()  #this is really important otherwise all changes lost
  #close connection
  conn.close()
  quit()

#If there are not values for the insert then we need to display the database contents.
#This can be done without an else statement since if there are values the script terminates.

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
</head>
<body>
<p><img src="https://www.freshnessmag.com/.image/t_share/MTM2NzkxNDE2MDE3MjY2Mjcz/the-acme-corporation-poster-by-bob-loukotka-01.jpg" alt = "ACME" width = "100" height = "100" style = "padding-right: 10px; padding-top: 0px; float:left"/></p>
<div class="Head">
<h1>ACME Talk</h1>
</div>

<div class="body">

</p>
<br>
<table class="col s6 offset-s3" border="1">
	<tr>
		<td>
""")

print ("""\
    <form action="messagePost.py" method="post">
    <p>
        <textarea id ="ta" rows="5" cols="50" name="talk"></textarea> <br />
<label for="ta">Talk anything and everything... </label>
<button class="btn waves-effect waves-light #c62828 red darken-3" type="submit" name="insert" style="display: block; margin: 0 auto;">Talk
<i class="material-icons right">record_voice_over</i>
</button>
    </p>
""")

message = message.printMessage(cursor)

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
</form>
</td>
</tr>
</table></div>
</body>
</html>
""");
