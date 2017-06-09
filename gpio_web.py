import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
on = GPIO.HIGH
off = GPIO.LOW

# Dictionary for pin
pins = {
    11 : {'color' : 'Red LED', 'state' : off},
    13 : {'color' : 'Green LED', 'state' : off}
}

# set each pin as an output
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, off)

@app.route('/')
def main():
    #read pin state and store it in pin dictionary
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
    #put the pin dictionary into template
    templateData = {
        'pins' : pins
    }
    return render_template('gpio_web.html', **templateData)

#if someone request pin number
@app.route('/<pinNum>/<action>')
def gpio_action(pinNum, action):
    # convert pin from the URL into an integer
    pinNum = int(pinNum)
    # get color
    ledColor = pins[pinNum]['color']
    # action is on, turn on the led
    if action == "on":
        GPIO.output(pinNum, on)
        web_msg = "Turned " + ledColor + " on."

    if action == "off":
        GPIO.output(pinNum, off)
        web_msg = "Turned " + ledColor + " off."

    if action == "toggle":
        GPIO.output(pinNum, not GPIO.input(pinNum))
        web_msg = "Toggled " + ledColor + "."

    # read the pin state and store in pins dictionary
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)

    #put datas into templateData
    templateData = {
        'message' : web_msg,
	'pins' : pins
    }

    return render_template('gpio_web.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
