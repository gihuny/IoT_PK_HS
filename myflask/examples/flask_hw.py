from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Main Page'

@app.route('/hello')
def hello_world():
    return 'KHL pi'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
