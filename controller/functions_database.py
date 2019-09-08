#!/usr/bin/env python3
import psycopg2


# FUNCTION TO CONNECT TO THE DATABASE -----------------------------------------
def connected():
    connect = psycopg2.connect(
        host='172.19.0.2',
        user='postgres',
        password='facauchere',
        dbname='ipspawn'
    )
    return connect


# FUNCTION TO INSERT ----------------------------------------------------------
def insert(connect, query):
    db = connect.cursor()
    db.execute(query)
    connect.commit()

# FUNCTION TO UPDATE ----------------------------------------------------------
def update(connect, query):
    db = connect.cursor()
    db.execute(query)
    connect.commit()

# FUNCTION TO SELECT ----------------------------------------------------------

def select(connect, query):
    db = connect.cursor()
    db_query = db.execute(query)
    db_select = db.fetchone()
    return db_select

# FUNCTION TO SELECT ----------------------------------------------------------

def get_id_user(connect, query):
    db = connect.cursor()
    db_query = db.execute(query)
    db_id_user = db.fetchone()
    return db_id_user
