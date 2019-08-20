#!/usr/bin/env python3

from bottle import Bottle, run, static_file, template, request
from beaker.middleware import SessionMiddleware
import datetime
import psycopg2
import os
from controller import connexion

action = Bottle()
sub_action = Bottle()

# GENERATION OF THE FOOTER & HEADER -------------------------------------------
footer = "./html/footer.html"
header = connexion.is_connected()

# INTIALISATION OF SESSIONS ---------------------------------------------------
session = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(action, session)


@action.get("/")
@action.get("/index.php")
def index():
    page = template(header)+template("./html/index.html")+template(footer)
    return page


# Sign up, in, out
@action.get("/sign_up.php")
@action.get("/sign_in.php")
def sign_up_or_sign_in_page():
    page = template(header)+template("./html/sign.html")+template(footer)
    return page


# SIGN UP ---------------------------------------------------------------------
@action.post("/sign_up.php")
def sign_up():
    from controller import subscribe
    # VERIFY THE USERS INPUT --------------------------------------------------
    checklist = subscribe.subscribe()
    # CREATE THE MESSAGE FOR THE ERRORS OR SUCCESS ----------------------------
    msg = subscribe.message_subscribe(checklist)
    page = template(header)+msg+template("./html/sign.html")+template(footer)
    return page


@action.post("/sign_in.php")
def sign_in():
    from controller import connexion
    checklist = connexion.login()
    page = connexion.redirection_login(checklist, header, footer)
    return page


@action.get("/sign_out.php")
def sign_out():
    connexion.disconnect()
    page = template(header)+template("./html/index.html")+template(footer)
    return page


# ACCOUNT ---------------------------------------------------------------------
@action.get("/account_settings.php")
def settings_page():
    return "settings page"


@action.post("/account_settings.php")
def save_changed_settings():
    return "save changed settings"


# Static
@action.get("/static/<filepath:path>")
def static(filepath):
    print(filepath)
    return static_file(filepath, root="./public")

# --------------------------------PICTURES-------------------------------------


@action.get('/style/pictures/png/<filename:re:.*.png>')
def send_image(filename):
    return static_file(
        filename,
        root='./style/pictures/png/',
        mimetype='image/png'
    )


run(app=app, host="192.168.1.8", port=9090, reloader=True, debug=True)
