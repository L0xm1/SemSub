# SSRF using url lib

import urllib.request
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    # Data from request object is passed to a new server-side request
    response = urllib.request.urlopen(url)
    return response.read()

if __name__ == '__main__':
    app.run(debug=True)
