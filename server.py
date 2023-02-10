# Command to run locally
# get ip with ipconfig and then wlan local area IPv4
# flask --app server run -h 192.168.137.1

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

if __name__ == '__main__':
    app.run(port=5000, host="192.168.137.1")