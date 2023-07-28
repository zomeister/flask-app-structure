#!/usr/bin/env python3

from flask import Flask # import flask

app = Flask(__name__) # flask constructor

@app.route("/")
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route("/<string:username>")
def name(username):
    return  f'<h1>Profile for {username}</h1>'

if __name__ == "__main__":
    app.run(port=5555, debug=True)