#!/bin/bash

source .venv/bin/activate
export FLASK_ENV=development
export FLASK_DEBUG=true
flask run --host=0.0.0.0 --port=5555