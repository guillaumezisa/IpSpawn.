#!/usr/bin/env python3

from bottle import Bottle, run

serv = Bottle()

@serv.get("/")
@serv.get("/index.php")
def index():
    return "Hello World"

run(serv, host="localhost", port=8080)
