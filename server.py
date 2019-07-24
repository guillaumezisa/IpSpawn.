#!/usr/bin/env python3

from bottle import Bottle, run, static_file, template

serv = Bottle()

#VOIR POUR LA VARIABLE DE SESSION:/
header="./html/header_offline.html"
footer="./html/footer.html"

@serv.get("/")
@serv.get("/index.php")
def index():
#    with open("./html/index.html", "r") as index_page:
#        return index_page.read()
    page =template(header)+template("./html/index.html")+template(footer)
    return page

# Sign up, in, out
@serv.get("/sign_up.php")
@serv.get("/sign_in.php")
def sign_up_or_sign_in_page():
    with open("./html/sign.html", "r") as sign_page:
        return sign_page.read()


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


# Static
@serv.get("/static/<filepath:path>")
def static(filepath):
    print(filepath)
    return static_file(filepath, root="./public")


run(serv, host="localhost", port=80)
