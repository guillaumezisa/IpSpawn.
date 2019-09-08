#!/usr/bin/env python3

from bottle import request, template
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


# FUNCTION TO OPEN A NEW SESSION AND CONNECT THE USER -------------------------
def redirection_login(checklist, header, footer):
    if(checklist["auth"] is True):
        # GATHER THE ID OF THE USER -------------------------------------------
        auth = {
            'email': request.forms.get("email"),
            'password': request.forms.get("password")
        }
        query = "SELECT id_user FROM USERS WHERE email='"+auth["email"]+"';"
        id_user = functions_database.get_id_user(connect, query)
        id = id_user[0]
        # ADD SESSION VARIABLES -----------------------------------------------
        s = request.environ.get('beaker.session')
        s['connected'] = s.get('connected', "yes")
        s['id_user'] = s.get('id_user', id)
        s.save()
        page = template("./html/header_online.html") + \
            template("./html/index.html") + template(footer)
        return page
    elif (checklist["auth"] is False):
        message = "<br>Les identifiants entrés ne correspondent pas,\
        ou n'éxistent pas.<br>"
        color = "bg-danger"
        message_banniere = "<div class='container-fluid "+color+"'><center>\
        "+message+"</center></div>"
        page = template(header) + message_banniere + template("\
        ./html/index.html")+template(footer)
        return page


# FUNCTION TO VERIFY IS THE USER IS CONNECT AND CHOOSE HEADER -----------------
def is_connected():
    s = request.environ.get('beaker.session')
    try:
        s["connected"]
    except (NameError, TypeError):
        header = "./html/header_offline.html"
    else:
        if(s["connected"] == "yes"):
            header = "./html/header_online.html"
    return(header)


# FUNCTION TO DELETE THE SESSION AND DISCONNECT THE USER ----------------------
def disconnect():
    s = request.environ.get('beaker.session')
    s.delete()
