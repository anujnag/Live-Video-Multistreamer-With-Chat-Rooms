#!/usr/bin/env python
import os
from importlib import import_module
from flask import Flask, render_template, Response

if os.environ.get('CAMERA'):
	Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
	from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/live_feed')
def live_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(host='0.0.0.0', threaded=True)
