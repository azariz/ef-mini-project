#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author : Amine Azariz

# * Imports
# --------------------------------------------------------------------------- *
from threading import local
from flask import Flask, request, jsonify

# * Params
# --------------------------------------------------------------------------- *


# * Config
# --------------------------------------------------------------------------- *
app = Flask(__name__)
app.DEBUG = True


# * Routes: Views
# --------------------------------------------------------------------------- *

# Index page
# --
@app.route('/')
def view_index():
    return '<p>Hello, World!</p>'


# * Routes: API
# @TODO: with more time, use Flask-RESTful instead
# --------------------------------------------------------------------------- *

# Events ressource
# --
@app.route('/events/', methods=['GET', 'POST'])
def api_events():

    # behaviour for POST request (adding an event)
    if request.method == 'POST':
        my_event = request.json
        app.logger.info(f"Received JSON is : {my_event}")
        return jsonify({'status':'ok'}), 200

    # behaviour for GET request (requesting all events)
    elif request.method == 'GET':
        return jsonify({'status':'not implemented.'}), 501