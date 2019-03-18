#!/bin/sh
export FLASK_APP=run.py
export FLASK_ENV=development
export DB_CONNECT=c5d5571d196b48272070c97c2d103041
pipenv run flask run -h 0.0.0.0