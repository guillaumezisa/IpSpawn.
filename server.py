#!/usr/bin/env python3

from bottle import Bottle, run, static_file, template, request
import datetime
import psycopg2
import os

serv = Bottle()

# LOAD HEADER & FOOTER --------------------------------------------------------
header = "./html/header_offline.html"
footer = "./html/footer.html"

# INDEX -----------------------------------------------------------------------
@serv.get("/")
@serv.get("/index.php")
def index():
    page = template(header)+template("./html/index.html")+template(footer)
    return page

# SIGN UP, IN, OUT ------------------------------------------------------------
@serv.get("/sign_up.php")
@serv.get("/sign_in.php")
def sign_up_or_sign_in_page():
    page = template(header)+template("./html/sign.html")+template(footer)
    return page


@serv.post("/sign_up.php")
def sign_up():
    from controller import subscribe


@serv.post("/sign_in.php")
def sign_in():
    return "sign in"


@serv.get("/sign_out.php")
def sign_out():
    return "sign out"


# ACCOUNT ---------------------------------------------------------------------
@serv.get("/account_settings.php")
def settings_page():
    return "settings page"


@serv.post("/account_settings.php")
def save_changed_settings():
    return "save changed settings"


# Static
@serv.get("/static/<filepath:path>")
def static(filepath):
    print(filepath)
    return static_file(filepath, root="./public")


# PICTURES---------------------------------------------------------------------
@serv.get('/style/pictures/png/<filename:re:.*\.png>')
def send_image(filename):
    root = "root='./style/pictures/png/'"
    return static_file(filename, root, mimetype='image/png')


run(serv, host="localhost", port=9090, reloader=True, debug=True)
