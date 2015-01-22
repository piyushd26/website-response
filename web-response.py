from flask import Flask, jsonify, request
import requests
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/response',  methods=['GET'])
def w_response():
    website = request.args.get('website')
    protocol = request.args.get('protocol')
    url = protocol + '://' + website

    start = time.time()
    r = requests.get(url)
    r.raw.read()
    end = time.time()
    t = int(round((end -start) * 1000))
    response_time = {}
    response_time['time'] = t

    return jsonify(response_time)

if __name__ == '__main__':
    app.run()
