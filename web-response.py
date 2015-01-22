from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/response/<website>')
def w_response(website):

    url = 'http://' + website

    start = time.time()
    r = requests.get(url)
    r.raw.read()
    end = time.time()
    t = str(int(round((end -start) * 1000)))
    response_time = {}
    response_time['time'] = t

    return jsonify(response_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
