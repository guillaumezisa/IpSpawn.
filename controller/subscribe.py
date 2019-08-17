#!/usr/bin/env python3

from bottle import request
import psycopg2, datetime

# IMPORT THE LOCAL MODULES -----------------------------------------------------
from controller import functions_database

# CONNEXION TO THE DATABASE ----------------------------------------------------
connect = psycopg2.connect( host='172.19.0.2', user='postgres', password='facauchere', dbname='ipspawn' )

# COLLECT INFORMATION ----------------------------------------------------------
email=request.forms.get("email")
pseudo=request.forms.get("pseudo")
pass1=request.forms.get("password")
pass2=request.forms.get("password_verification")
points="1"
status="1"
pp="profiles_pictures/nopic.png"
date=str(datetime.date.today())

# FUNCTION TO VERIFY IF THE PASSWORDS MATCH ------------------------------------
pass_check = functions_database.verify_pass(pass1,pass2)
if ( pass_check == 1 ):
    print("redirection error pass 1")
elif ( pass_check == 2 ):
    print("redirection error pass 2")
elif ( pass_check == 3 ):
    print("redirection error pass 3")
elif ( pass_check == 0 ):
    # FUNCTION TO VERIFY IF THE MAIL IS ALREADY TAKEN --------------------------
    query = "SELECT COUNT(EMAIL) FROM USERS WHERE EMAIL = '"+email+"';"
    email_check = functions_database.verify_email(connect,email,query)
    formated_email_check = functions_database.format_count(email_check)
    if ( formated_email_check != 0 ):
        print("redirection error email exist")
    else :
        # FUNCTION TO VERIFY IF THE PSEUDO IS ALREADY TAKEN --------------------
        query = "SELECT COUNT(PSEUDO) FROM USERS WHERE PSEUDO = '"+pseudo+"';"
        pseudo_check = functions_database.verify_pseudo(connect,pseudo,query)
        formated_pseudo_check = functions_database.format_count(pseudo_check)
        if ( formated_pseudo_check != 0 ):
            print("redirection error pseudo exist")
        else :
            # FINALLY INSERT TO THE DATABASE -----------------------------------
            query="INSERT INTO USERS (EMAIL,PSEUDO,PASSWORD,POINTS,STATUS,PP,DATES)VALUES ('"+email+"','"+pseudo+"','"+pass1+"','"+points+"','"+status+"','"+pp+"','"+date+"');"
            functions_database.insert( connect,query )
            print("A new user as been created")
