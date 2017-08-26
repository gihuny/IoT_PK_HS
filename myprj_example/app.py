#!/usr/bin/env python
from flask import Flask, render_template, Response

# emulated camera
# from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)

@app.route('/video/<action>')
def video_onoff(action):
    video_on = True
    if action == 'on':
        video_on = True
    elif action == 'off':
        video_on = False
    else:
        pass

    templateData = {
        'video_on' : video_on
    }
    
    return render_template('index.html', **templateData)

@app.route('/')
def index():
    """Video streaming home page."""

    templateData = {
        'video_on' : True
        }
    
    return render_template('index.html', **templateData)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
