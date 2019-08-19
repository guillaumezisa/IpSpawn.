#!/usr/bin/env python3.6


# FUNCTION AUTHENTIFICATION ---------------------------------------------------
def auth(connect, query):
    db = connect.cursor()
    db_query = db.execute(query)
    db_auth = db.fetchone()
    return db_auth
