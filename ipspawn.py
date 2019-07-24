#!/usr/bin/python

from bottle import Bottle, run, template
app = Bottle()

@app.route('/')
def index():
	return template("index.tpl")

run(app,host="localhost",port=80)
