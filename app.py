#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author : Amine Azariz

# * Imports
# --------------------------------------------------------------------------- *
from flask import Flask, request, jsonify
from time import time
from flask_cors import CORS
import jwt
import requests
import json

# * Params
# --------------------------------------------------------------------------- *
ZOOM_API = 'https://api.zoom.us/v2/users/me/meetings'
ZOOM_KEY = 'asl8P-7OQ2iY6-QjxzV70A'
ZOOM_SECRET = 'oUWLZSxyxiPMAleDrgA4lMv13G4qFUoLgtfR'
ZOOM_KEY_EXPIRY = 5000  # seconds

# * Config
# --------------------------------------------------------------------------- *
app = Flask(__name__)
CORS(app)


# * Utils
# --------------------------------------------------------------------------- *

# Zoom Get Token
# generate a new JWT token for the ZOOM API
def zoom_get_token():
    token = jwt.encode(
        {'iss': ZOOM_KEY, 'exp': time() + 5000},
        ZOOM_SECRET,
        algorithm='HS256'
    )
    return token


# Zoom New Meeting
# transform front data event to a meeting event
def zoom_new_meeting(user_event):
    event_data = {"topic": user_event['event_title'],
                  "type": 2,  # scheduled meeting
                  "start_time": user_event['event_start'],  # GMT timestring
                  "duration": user_event['event_duration'],  # minutes
                  "timezone": "Europe/Paris"  # @TODO: Get from client browser
                  }
    return event_data


# Zoom Post Event
# fetch zoom api and get returns
def zoom_post_event(event_data):
    # prepare request
    headers = {'authorization': 'Bearer %s' % zoom_get_token(),
               'content-type': 'application/json'}

    # post to zoom api
    zoom_request = requests.post(ZOOM_API, headers=headers,
                                 data=json.dumps(event_data))

    # jsonify the zoom response to a dict
    zoom_response = json.loads(zoom_request.text)
    return zoom_response


# * Routes: Views
# --------------------------------------------------------------------------- *

# Index page
# --
@app.route('/')
def view_index():
    return '<p>Hello there. Please use <pre>/api/events/</pre> endpoint.</p>'


# * Routes: API
# @TODO: with more time, use Flask-RESTful instead
# --------------------------------------------------------------------------- *

# Events ressource
# --
@app.route('/api/events/', methods=['GET', 'POST'])
def api_events():

    if request.method == 'POST':
        # behaviour for POST request (adding an event)
        # parse data front front
        user_event = request.json
        app.logger.debug(f"Received JSON from front:\n {user_event}")

        # create a zoom meeting then post it to API
        zoom_meeting_data = zoom_new_meeting(user_event)
        app.logger.debug(f"Creating meeting on Zoom:\n {zoom_meeting_data}")
        res = zoom_post_event(zoom_meeting_data)
        app.logger.debug(f"Meeting created. Details:\n {res}")

        # if all good, return OK
        return jsonify({'status': 'ok', 'zoom_res': res}), 200

    elif request.method == 'GET':
        # behaviour for GET request (requesting all events)
        return jsonify({'status': 'not implemented.'}), 501
