#!/usr/bin/env python3

#adapted from http://webpython.codepoint.net
#script to create or continue a session; time of last visit will be stored in a session variable

import hashlib, time, os, shelve
from http import cookies

import cgitb;

#creates/continues a session and exposes the session as a dictionary
def start():
    #try to read the 'sid' cookie
    cookie = cookies.SimpleCookie()
    string_cookie = os.environ.get('HTTP_COOKIE')

    if not string_cookie:
       #create the 'sid' cookie if no cookies exist
       sid = hashlib.sha256(repr(time.time()).encode()).hexdigest()
       cookie['sid'] = sid
       message = 'New session'
    else:
       #try to read the 'sid' cookie (not just any cookie)
       cookie.load(string_cookie)
       if 'sid' in cookie:
         #read the 'sid'
         sid = cookie['sid'].value
       else:
         #create new sid ans store it in a cookie
         sid = hashlib.sha256(repr(time.time()).encode()).hexdigest()
         cookie['sid'] = sid
         # message = 'New session'
    cookie['sid']['expires'] = 12 * 30 * 24 * 60 * 60

    #print the cookie to tell the browser to set it
    print (cookie)
    #print start html

    # The shelve module will persist the session data
    # and expose it as a dictionary
    #open the session file (this also creates it if it does not exist)
    session_file = '/tmp/sess_' + sid
    session = shelve.open(session_file, writeback=True)

    # Retrieve last visit time from the session
    #lastvisit = session['lastvisit']
    # lastvisit = session.get('lastvisit')
    # if lastvisit:
    #    message = 'Welcome back. Your last visit was at ' + \
    #       time.asctime(time.localtime(float(lastvisit)))
    # Save the current time in the session
    session['lastvisit'] = repr(time.time())

    return session


#close session file handler
def end(session):

    session.close()
