#! /usr/bin/env python
# coding: utf-8

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello main application"

@app.route("/sub")
def sub():
    return "Hello sub application"
