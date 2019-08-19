#!/usr/bin/env python3

from bottle import request
import datetime


# IMPORT THE LOCAL MODULES ----------------------------------------------------
from controller import functions_database

# CONNEXION TO THE DATABASE ---------------------------------------------------
connect = functions_database.connected()

# FUNCTION TO VERIFY IF THE PASSWORD IS CORRECT -------------------------------
def verify_pass(pass1, pass2):
    if (pass1 != pass2):
        return 1
    elif (len(pass1) < 4):
        return 2
    elif (len(pass1) > 50):
        return 3
    else:
        return 0


# FUNCTION TO VERIFY IF THE EMAIL IS NOT ALREADY EXISTING ---------------------
def verify_email(connect, email, query):
    db = connect.cursor()
    db_query = db.execute(query)
    db_email = db.fetchone()
    return db_email


# FUNCTION TO VERIFY IF THE PSEUDO IS NOT ALREADY EXISTING --------------------
def verify_pseudo(connect, pseudo, query):
    db = connect.cursor()
    db_query = db.execute(query)
    db_pseudo = db.fetchone()
    return db_pseudo

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
    # CL = CHECKLIST
    cl = {
        "pass": "0",
        "email": "0",
        "pseudo": "0"
    }
    # FUNCTION TO VERIFY IF THE PASSWORDS MATCH -------------------------------
    pass_check = verify_pass(
        subscriber["pass1"], subscriber["pass2"]
    )
    if (pass_check == 1):
        cl["pass"] = "Le mot de passe n'est pas identique."
    elif (pass_check == 2 or pass_check == 3):
        cl["pass"] = "Le mot de passe doit faire \
        entre 4 et 50 charactères."
    elif (pass_check == 0):
        cl["pass"] = True

    # FUNCTION TO VERIFY IF THE MAIL IS ALREADY TAKEN -------------------------
    query = "SELECT COUNT(EMAIL)\
        FROM USERS\
        WHERE EMAIL ='{email}';\
    ".format(email=subscriber["email"])

    email_check = verify_email(
        connect, subscriber["email"], query
        )

    if (email_check[0] != 0):
        cl["email"] = "L'email entrée existe déjà."
    else:
        cl["email"] = True

    # FUNCTION TO VERIFY IF THE PSEUDO IS ALREADY TAKEN -----------------------
    query = "SELECT COUNT(PSEUDO)\
        FROM USERS\
        WHERE PSEUDO = '{psd}';".format(psd=subscriber["pseudo"])

    pseudo_check = verify_pseudo(
        connect, subscriber["pseudo"], query
    )
    if (pseudo_check[0] != 0):
        cl["pseudo"] = "Le pseudo choisit éxiste déjà."
    else:
        cl["pseudo"] = True

    if (cl["pass"] and cl["email"] and cl["pseudo"]):
        # FINALLY INSERT TO THE DATABASE --------------------------------------
        query = "INSERT INTO USERS \
            (EMAIL,PSEUDO,PASSWORD,POINTS,STATUS,PP,DATES)VALUES \
            ('"+subscriber["email"]+"','"+subscriber["pseudo"]+"',\
            '"+subscriber["pass1"]+"','"+subscriber["points"]+"',\
            '"+subscriber["status"]+"','"+subscriber["pp"]+"',\
            '"+subscriber["date"]+"');"

        functions_database.insert(connect, query)

    return cl


def message_subscribe(cl):
    message = "<br>"
    if (cl["pass"] is True and cl["email"] is True and cl["pseudo"] is True):
        message = "Vous avez bien été enregistré."
        color = "bg-success"
    if (cl["email"] is not True):
        message = message + cl['email'] + "<br>"
        color = "bg-danger"
    if (cl["pseudo"] is not True):
        message = message + cl['pseudo'] + "<br>"
        color = "bg-danger"
    if (cl["pass"] is not True):
        message = message + cl['pass'] + "<br>"
        color = "bg-danger"
    message = message + "<br>"
    message_banniere = "<div class='container-fluid " + color + "'><center>\
    " + message + "</center></div>"
    return message_banniere
