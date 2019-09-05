#!/usr/bin/env python3
import psycopg2


# FUNCTION TO CONNECT TO THE DATABASE -----------------------------------------
def connected():
    connect = psycopg2.connect(
        host='172.19.0.3',
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
