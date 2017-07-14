import clock_by_7seg # 7-seg run module
#from flask import Flask 

#app = Flask(__name__)

#@app.route('/')
#def mainpage():
#    now = datetime.datetime.now()
#    timeString = now.strftime("%Y-%m-%d %H:%M")
#    templateData = {
#        'title' : 'Current Time',
#        'time': timeString,
#        'onoff' : 'off'
#    }

if __name__ == "__main__":
 clock_by_7seg.clock_onoff(on = True)
