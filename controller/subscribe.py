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

if pass_check == 1 :
    print("Error : password not corresponding")
elif pass_check == 2 :
    print("Error : password too small")
elif pass_check == 3 :
    print("Error : password too large")
elif pass_check == 0 :
    # FUNCTION TO VERIFY IF THE MAIL AND PSEUDO ARE NOT ALREADY TAKEN --------------


# FINALLY INSERT TO THE DATABASE -----------------------------------------------
query="INSERT INTO USERS (EMAIL,PSEUDO,PASSWORD,POINTS,STATUS,PP,DATES)VALUES ('"+email+"','"+pseudo+"','"+pass1+"','"+points+"','"+status+"','"+pp+"','"+date+"');"
functions_database.insert( connect,query )
print("A new user as been created")
