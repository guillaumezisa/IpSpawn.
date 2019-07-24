#!/usr/bin/env python3

from bottle import Bottle, run

serv = Bottle()

@serv.get("/")
@serv.get("/index.php")
def index():
    return "Hello World"

# Sign up, in, out
@serv.get("/sign_up.php")
@serv.get("/sign_in.php")
def sign_up_or_sign_in_page():
    return "sign up and sign ip page"


@serv.post("/sign_up.php")
def sign_up():
    return "sign up"


@serv.post("sign_in.php")
def sign_in():
    return "sign in"


@serv.get("/sign_out.php")
def sign_out():
    return "sign out"


# Account
@serv.get("/account_settings.php")
def settings_page():
    return "settings page"


@serv.post("/account_settings.php")
def save_changed_settings():
    return "save changed settings"

run(serv, host="localhost", port=8080)
