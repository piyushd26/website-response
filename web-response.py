from flask import Flask
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
    r = requests.get(url, timeout=3)
    r.raw.read()
    end = time.time()
    t = end - start
    return '%d' % int(round(t * 1000))


if __name__ == '__main__':
    app.run()
