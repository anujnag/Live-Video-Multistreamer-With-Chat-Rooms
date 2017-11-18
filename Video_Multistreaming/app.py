#!/usr/bin/env python
import os
from importlib import import_module
from flask import Flask, render_template, Response

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

app = Flask(__name__)

music_dir = './static/music'
video_dir = './static/video'


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/static_content_m')
def index2():
    music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
    music_files_number = len(music_files)
    return render_template("index2.html", title='Home', music_files_number=music_files_number, music_files=music_files)        

@app.route('/music/<filename>')
def song(filename):
    return render_template('play.html', title=filename, music_file=filename)

@app.route('/static_content_v')
def index3():
    video_files = [f for f in os.listdir(video_dir) if f.endswith('mp4')]
    video_files_number = len(video_files)
    return render_template("index3.html", title='Home', video_files_number=video_files_number, video_files=video_files)

@app.route('/video/<filename>')
def video(filename):
    return render_template('play2.html', title=filename, video_file=filename)        

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
