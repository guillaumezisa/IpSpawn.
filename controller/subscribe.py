#!/usr/bin/env python3

from bottle import request
import psycopg2
import datetime


# IMPORT THE LOCAL MODULES ----------------------------------------------------
from controller import functions_database
from controller import functions_subscribe

# CONNEXION TO THE DATABASE ---------------------------------------------------
connect = psycopg2.connect(
    host='172.19.0.2',
    user='postgres',
    password='facauchere',
    dbname='ipspawn'
)


# FUNCTION SUBSCRIBE
def subscribe():
    # COLLECT INFORMATION -----------------------------------------------------
    subscriber = {
        'email': request.forms.get("email"),
        'pseudo': request.forms.get("pseudo"),
        'pass1': request.forms.get("password"),
        'pass2': request.forms.get("password_verification"),
        'points': "1",
        'status': "1",
        'pp': "profiles_pictures/nopic.png",
        'date': str(datetime.date.today())
    }
    checklist = {
        "pass": "0",
        "email": "0",
        "pseudo": "0"
    }
    # FUNCTION TO VERIFY IF THE PASSWORDS MATCH -------------------------------
    pass_check = functions_subscribe.verify_pass(
        subscriber["pass1"], subscriber["pass2"]
    )
    if (pass_check == 1):
        checklist["pass"] = "Le mot de passe n'est pas identique."
    elif (pass_check == 2 or pass_check == 3):
        checklist["pass"] = "Le mot de passe doit faire \
        entre 4 et 50 charactères."
    elif (pass_check == 0):
        checklist["pass"] = True

    # FUNCTION TO VERIFY IF THE MAIL IS ALREADY TAKEN -------------------------
    query = "SELECT COUNT(EMAIL)\
        FROM USERS\
        WHERE EMAIL ='{email}';\
    ".format(email=subscriber["email"])

    email_check = functions_subscribe.verify_email(
        connect, subscriber["email"], query
        )

    if (email_check[0] != 0):
        checklist["email"] = "L'email entrée existe déjà."
    else:
        checklist["email"] = True

    # FUNCTION TO VERIFY IF THE PSEUDO IS ALREADY TAKEN -----------------------
    query = "SELECT COUNT(PSEUDO)\
        FROM USERS\
        WHERE PSEUDO = '{psd}';".format(psd=subscriber["pseudo"])

    pseudo_check = functions_subscribe.verify_pseudo(
        connect, subscriber["pseudo"], query
    )
    if (pseudo_check[0] != 0):
        checklist["pseudo"] = "Le pseudo choisit éxiste déjà."
    else:
        checklist["pseudo"] = True

    if (checklist["pass"] and checklist["email"] and checklist["pseudo"]):
        # FINALLY INSERT TO THE DATABASE --------------------------------------
        query = "INSERT INTO USERS \
            (EMAIL,PSEUDO,PASSWORD,POINTS,STATUS,PP,DATES)VALUES \
            ('"+subscriber["email"]+"','"+subscriber["pseudo"]+"',\
            '"+subscriber["pass1"]+"','"+subscriber["points"]+"',\
            '"+subscriber["status"]+"','"+subscriber["pp"]+"',\
            '"+subscriber["date"]+"');"

        functions_database.insert(connect, query)

    return checklist
