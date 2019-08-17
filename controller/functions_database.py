#!/usr/bin/env python3

# FUNCTION TO INSERT
def insert( connect , query ) :
      db = connect.cursor()
      db.execute( query )
      connect.commit()

# FUNCTION TO VERIFY IF THE PASSWORD IS CORRECT
def verify_pass ( pass1 , pass2 ):
    if ( pass1 != pass2 ):
        return 1
    elif ( len(pass1) < 4 ) :
        return 2
    elif ( len(pass1) > 50 ) :
        return 3
    else :
        return 0

# FUNCTION TO VERIFY IF THE EMAIL IS NOT ALREADY EXISTING
def verify_email ( connect,email,query ):
    db = connect.cursor()
    db_query = db.execute(query)
    db_email = db.fetchone()
    return db_email

# FUNCTION TO VERIFY IF THE PSEUDO IS NOT ALREADY EXISTING
def verify_pseudo ( connect,pseudo,query ):
    db = connect.cursor()
    db_query = db.execute(query)
    db_pseudo = db.fetchone()
    return db_pseudo

# FUNCTION TO FORMAT THE RESULT OF COUNT QUERY
def format_count ( count ):
    count = count[1:len(count)-2]
    return int(count)

# FUNCTION XOR AND OTHERS FOR PASSWORDS
#def secure_my_string ( string ):
