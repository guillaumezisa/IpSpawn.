#!/usr/bin/env python3
import psycopg2


# CONNEXION VARIABLES ---------------------------------------------------------
hostname = '172.19.0.2'


username = 'postgres'
password = 'facauchere'
database = 'ipspawn'
connect = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

# FONCTION DE SELECT
def select( connect , query ) :
    db = connect.cursor()
    db.execute( query )
    print(db.fetchall())

# FONCTION D'INSERT
def insert( connect , query ) :
    db = connect.cursor()
    db.execute( query )
    connect.commit()

# A UTILISER DANS L'INSCRIPTION ECT
query="INSERT INTO USERS (EMAIL,PSEUDO,PASSWORD,POINTS,PP,STATUS,DATES)VALUES ( 'zacsqcqsa', 'jacky', '123', 1, 'sex', 1, '2019-08-15');"
insert( connect,query )
query="SELECT PSEUDO,EMAIL FROM USERS"
select( connect,query )
connect.close()
