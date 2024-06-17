#path traversal using open 

import flask
import os

app = flask.Flask(__name__)

@app.route('/download')
def download_file():
    filename = flask.request.args.get('filename')
    # Found request data in a call to 'open'
    file = open(filename, 'rb')
    return flask.send_file(file, attachment_filename=filename)

if __name__ == '__main__':
    app.run()
