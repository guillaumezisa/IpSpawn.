#!/usr/bin/env python3

from bottle import Bottle, run, static_file, template, request
from beaker.middleware import SessionMiddleware
import datetime
import psycopg2
import os
from controller import connexion
from controller import view_account_settings

action = Bottle()
sub_action = Bottle()

# GENERATION OF THE FOOTER & HEADER -------------------------------------------
footer = "./html/footer.html"
header = connexion.is_connected()

# INTIALISATION OF SESSIONS ---------------------------------------------------
session = {
    'session.type': 'file',
    'session.cookie_expires':3600,
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
    s = request.environ.get('beaker.session')
    body = view_account_settings.gen(s['id_user'])
    page = template(header)+body+template(footer)
    return page


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

@action.get('/profile_pictures/<filename:re:.*.png>')
def send_image(filename):
    return static_file(
        filename,
        root='./profile_pictures/',
        mimetype='image/png'
    )

@action.get('/profile_pictures/<filename:re:.*.jpg>')
def send_image(filename):
    return static_file(
        filename,
        root='./profile_pictures/',
        mimetype='image/jpg'
    )
# UPLOAD PICTURE PROFILE ------------------------------------------------------
@action.post('/upload')
def do_upload():
    from controller import functions_database
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    s = request.environ.get('beaker.session')
    save_path = "profile_pictures/"+str(s["id_user"])+ext
    if(os.path.exists(save_path)):
        os.remove(save_path)
    upload.save(save_path) # appends upload.filename automatically
    query = "UPDATE USERS SET pp='"+save_path+"' WHERE id_user='"+str(s["id_user"])+"';"
    functions_database.update(functions_database.connected(), query)

    return 'OK'


run(app=app, host="192.168.1.8", port=9090, reloader=True, debug=True)
