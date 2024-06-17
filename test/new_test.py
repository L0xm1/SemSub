from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_input = request.args.get('input', 'default_value')
    # Vulnerable template string using format()
    template = 'Hello, {}!'.format(user_input)
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True)





## SHA1 SAMPLE
# from cryptography.hazmat.primitives.hashes import SHA1

# # Using SHA1 hash algorithm (considered insecure)
# hash_algorithm = SHA1()


# Empty AES

# from Crypto.Cipher import AES

# # Potential empty AES encryption key
# input=""
# input="test"
# empty_key = AES.new(input, AES.MODE_ECB)



##insecure deserialization

# import pickle
# from flask import Flask

# app = Flask(__name__)

# # Flask route using insecure deserialization
# @app.route('/')
# def index():
#     serialized_data = request.args.get('data')
#     deserialized_data = pickle.loads(serialized_data)
#     return 'Success'

# if __name__ == '__main__':
#     app.run(debug=True)



## JWT None 

# import jwt

# # Detected use of 'none' algorithm in JWT token
# token = jwt.encode({'some': 'payload'}, algorithm='none')



## send_file without path sanitization 

# from flask import Flask, send_file

# app = Flask(__name__)

# @app.route('/download/<filename>')
# def download_file(filename):
#     return send_file(filename)

# if __name__ == '__main__':
#     app.run(debug=True)




##path traversal using open 

# import flask
# import os

# app = flask.Flask(__name__)

# @app.route('/download')
# def download_file():
#     filename = flask.request.args.get('filename')
#     # Found request data in a call to 'open'
#     file = open(filename, 'rb')
#     return flask.send_file(file, attachment_filename=filename)

# if __name__ == '__main__':
#     app.run()



## SSRF using url lib

# import urllib.request
# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     url = request.args.get('url')
#     # Data from request object is passed to a new server-side request
#     response = urllib.request.urlopen(url)
#     return response.read()

# if __name__ == '__main__':
#     app.run(debug=True)
