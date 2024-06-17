#insecure deserialization

import pickle,requests
from flask import Flask

app = Flask(__name__)

# Flask route using insecure deserialization
@app.route('/')
def index():
    serialized_data = requests.args.get('data')
    deserialized_data = pickle.loads(serialized_data)
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)

