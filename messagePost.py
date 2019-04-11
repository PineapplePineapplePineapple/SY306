#!/usr/bin/env python3
import cgi,cgitb
from message import message

cgitb.enable()

import mysql.connector
from mysql.connector import errorcode

import config

try:
  cnx = mysql.connector.connect(user=config.USER,
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

#create cursor to send queries
cursor = cnx.cursor()

#see if needed to insert data - get parameters from the form
params = cgi.FieldStorage()
insertButton = params.getvalue("insert")

#if insert button was pushed
if insertButton:

  content = params.getvalue("talk")
  result = song.addMessage(cursor, content, time)
  #print either a confirmation message or error message
  if result==1:

    print('Status: 303 See Other')
    print('Location: songPage.py')
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
   <meta http-equiv="refresh" content="5; url=songPage.py">
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
  cnx.commit()  #this is really important otherwise all changes lost
  #close connection
  cnx.close()
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
<title>DB connection with Python</title>
<style type = "text/css">
table, td, th {border:1px solid black}
</style>
</head>
<body>
""")
#create the page
print ("<h1>Favorite songs</h1>")

print ('<form method = "post" action = "songPage.py">')

#get songs from database by calling the printSongs function in song
message = song.printMessage(cursor)

#print the table with songs, or "No songs in db message"
if message:
  print (message)
else:
  print ("<h2>No songs in database</h2>")

#print the inputs for getting the artist and title, and a submit button to insert
print ("""\
<p>
<label>Artist: <input type = "text" name = "artist"></label><br>
<label>Title: <input type = "text" name = "title"></label><br>
<input type = "submit" name = "insert" value = "Insert song">
</p>""")

print ("</form>")

#close cursor since we don't use it anymore
cursor.close()

#commit the transaction
cnx.commit()  #this is really important otherwise all changes lost

#close connection
cnx.close()

#print end html tags
print("</body></html>");
