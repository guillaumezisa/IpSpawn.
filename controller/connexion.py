#!/usr/bin/env python3

from bottle import request
import bottle_session

# IMPORT THE LOCAL MODULES ----------------------------------------------------
from controller import functions_database
from controller import functions_connexion

# CONNEXION TO THE DATABASE ---------------------------------------------------
connect = functions_database.connected()


def login():
    auth = {
        'email': request.forms.get("email"),
        'password': request.forms.get("password")
    }
    checklist = {
        "auth": "0"
    }

    # FUNCTION TO VERIFY IF THE PASSWORDS MATCH -------------------------------
    query = "SELECT COUNT(PASSWORD)\
        FROM USERS\
        WHERE EMAIL = '{email}'\
        AND PASSWORD = '{password}';\
        ".format(email=auth["email"], password=auth["password"])

    pass = functions_connexion.auth(functions_database.connected(), query)

    if(pass[0] == 1):
        checklist["auth"] = True
    else:
        checklist["auth"] = False

    return(checklist)


def redirection_login(checklist):
    if(checklist is True):
        print("CONNECTED")
        # SESSION OPEN
        session['status_now'] = "online"
        # user_name = session.get('name')
        page = template(header)+template("./html/index.html")+template(footer)
        return page
    elif (checklist is False):
        message = "<br>Les identifiants entrés ne correspondent pas,\
        ou n'éxistent pas.<br>"
        color = "bg-danger"
        message_banniere = "<div class='container-fluid "+color+"'><center>\
        "+message+"</center></div>"
        return message_banniere
