#!/usr/bin/env python3

def insert( connect , query ) :
      db = connect.cursor()
      db.execute( query )
      connect.commit()

#def secure_my_string ( string ):

def verify_pass ( pass1 , pass2 ):
    if ( pass1 != pass2 ):
        return "1"
    elif ( len(pass1) < 4 ) :
        return "2"
    elif ( len(pass1) > 50 ) :
        return "3"
    else :
        return "0"



def verify_email ( email ):
    return "email"

def verify_pseudo ( pseudo):
    return "pseudo"
