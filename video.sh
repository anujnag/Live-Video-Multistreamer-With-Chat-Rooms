#!/bin/sh
cd Video_Multistreaming/
gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 app:app