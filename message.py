# message.py
#
# Jacob Harrison

import mysql.connector

class message:

  def __init__(self):
    pass

  def addMessage(cursor, content):

    #create query statement
    query = "Insert into MESSAGES(Content, Time) values ('" + content + "','" + time + "')"
    #execute the query
    try:
      cursor.execute(query)
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
    query = "SELECT Username, Content, Time FROM USERS, MESSAGES, MESSAGES_POSTED WHERE USERS.UID = MESSAGES_POSTED.UID AND MESSAGES.MID = MESSAGES_POSTED.MID ORDER BY Time"
    try:
      cursor.execute(query)
    except mysql.connector.Error as err:
      #for DEBUG only we'll print the error and statement- we should print some generic message instead for production site
      print ('<p style = "color:red">')
      print(err)
      print (" for statement" + cursor.statement )
      print ('</p>')

    nbRows = 0

    for (Username, Content, Time) in cursor:

       newmessages += "<tr><td><span style=\"color:white\">"+str(Time) + "</span><span style=\"color:red\">" + str(Username)+"</span>"+str(Content)+ "</td></tr>\n"
       nbRows+=1

    if nbRows > 0:
      return table
    else:
      return ""
