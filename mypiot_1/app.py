#!/usr/bin/env python
from flask import Flask, render_template, Response, request, redirect, url_for, session
import RPi.GPIO as GPIO

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

# init settings
app = Flask(__name__)
on = GPIO.HIGH
off = GPIO.LOW
LEDpinNum = 11
CAMpinNum = 13

# GPIO get functions.
def get_gpio_state(pinNum):
    gpio_state = GPIO.input(pinNum)
    return gpio_state

def get_led_msg(gpio_state):
    if gpio_state == on:
        led_msg = "LED 상태: on"
    else:
        led_msg = "LED 상태: off"
    return led_msg

#init setup
if __name__ == '__main__':
#    video_on = True

    #init GPIO
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)

    #LED pin
    GPIO.setup(LEDpinNum, GPIO.OUT)
    led_msg = get_led_msg(get_gpio_state(LEDpinNum))
    
    #Camera state pin
    GPIO.setup(CAMpinNum, GPIO.OUT)

#URL setup
@app.route('/')
def index():
    video_on = bool(GPIO.input(CAMpinNum))
    led_msg = get_led_msg(get_gpio_state(LEDpinNum))

    templateData = { 
        'video_on' : video_on,
        'message' : led_msg
    }
    """Video streaming home page."""
    return render_template('index.html', **templateData)

@app.route('/video/<action>')
def video_stream_off(action):
    if action == "on":
        GPIO.output(CAMpinNum, on)
    else:
        GPIO.output(CAMpinNum, off)

    return redirect(url_for('index'))

@app.route('/led/<action>')
def gpio_action(action):
    # action is on, turn on the led
    if action == "on":
        GPIO.output(LEDpinNum, on)

    if action == "off":
        GPIO.output(LEDpinNum, off)

    if action == "toggle":
        GPIO.output(LEDpinNum, not GPIO.input(LEDpinNum))

    return redirect(url_for("index"))

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
