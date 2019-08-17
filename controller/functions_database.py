#!/usr/bin/env python3


# FUNCTION TO INSERT
def insert(connect, query):
    db = connect.cursor()
    db.execute(query)
    connect.commit()
