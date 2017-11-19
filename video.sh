#!/bin/sh
cd Video_Multistreaming/
CAMERA=opencv python app.py
#CAMERA=opencv gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5002 app:app
