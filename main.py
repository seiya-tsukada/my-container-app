#! /usr/bin/env python
# coding: utf-8

from flask import Flask, request, render_template
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def index():

    req_info = dict()
    req_info["user_agent"] = request.headers.get("User-Agent")
    req_info["accept"] = request.headers.get("Accept")
    req_info["accept_language"] = request.headers.get("Accept-Language")
    req_info["accept_encoding"] = request.headers.get("Accept-Encoding")

    return render_template("index.html", req_info=req_info)

@app.route("/sub")
def sub():
    return "Hello sub application"
