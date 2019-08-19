#!/usr/bin/env python3

from bottle import request
import bottle_session

# IMPORT THE LOCAL MODULES ----------------------------------------------------
from controller import functions_database

# CONNEXION TO THE DATABASE ---------------------------------------------------
connect = functions_database.connected()

# FUNCTION AUTHENTIFICATION ---------------------------------------------------
def authentification(connect, query):
    db = connect.cursor()
    db_query = db.execute(query)
    db_auth = db.fetchone()
    return db_auth

# FUNCTION TO VERIFY IF THE PASSWORDS MATCH -----------------------------------
def login():
    auth = {
        'email': request.forms.get("email"),
        'password': request.forms.get("password")
    }
    checklist = {
        "auth": "0"
    }

    query = "SELECT COUNT(PASSWORD)\
        FROM USERS\
        WHERE EMAIL = '{email}'\
        AND PASSWORD = '{password}';\
        ".format(email=auth["email"], password=auth["password"])

    passw = authentification(functions_database.connected(), query)

    if(passw[0] == 1):
        checklist["auth"] = True
    else:
        checklist["auth"] = False

    return(checklist)


def redirection_login(checklist):
    if(checklist is True):
        print("CONNECTED")
        # SESSION OPENING -----------------------------------------------------
        session['status_now'] = "online"
        s = request.environ.get('beaker.session')
        s['connected'] = s.get('connected', "yes")
        s.save()
        #return s['connected']
        page = template(header)+template("./html/index.html")+template(footer)
        return page
    elif (checklist is False):
        message = "<br>Les identifiants entrés ne correspondent pas,\
        ou n'éxistent pas.<br>"
        color = "bg-danger"
        message_banniere = "<div class='container-fluid "+color+"'><center>\
        "+message+"</center></div>"
        return message_banniere

def is_connected():
    s = request.environ.get('beaker.session')
    try:
        s["connected"]
    except (NameError,TypeError):
        header = "./html/header_offline.html"
    else:
        if(s["connected"] == "yes"):
            header = "./html/header_online.html"
    return(header)
