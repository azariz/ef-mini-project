#!/bin/bash

source .venv/bin/activate
export FLASK_ENV=development
export FLASK_DEBUG=true
flask run