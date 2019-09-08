#!/usr/bin/env python3
from controller import functions_database
def gen(session_id_user):
    # TOP OF THE PAGE ---------------------------------------------------------
    page1 = "\
    <div class='position-relative overflow-hidden p-3 p-md-5 m-md-3 \
    text-center bg-light'><div class='container'>\
    <h2>Gestion du compte</h2><br><div class='row'>\
    <div class='col-4'><h4> Changer d'image de profile </h4><br>"
    connect = functions_database.connected()
    query = "SELECT pp FROM users WHERE id_user='"+str(session_id_user)+"'"
    path = functions_database.select(connect, query)
    pp = "<img width='100px'src='"+path[0]+"'>"
    page2 = "<br><br><form action='/upload' method='post' enctype='multipart/form-data'>\
    <button class='btn btn-success'><input type='file' class='custom-file-input' lang='fr' value='aaa'></button>\
    <button class='btn btn-danger'/>Enregistrer</button></form></div></div></div>\
    <div class='product-device shadow-sm d-none d-md-block'></div>\
    <div class='product-device product-device-2 shadow-sm d-none d-md-block'></div></div>"

    page = page1+pp+page2
    return(page)
