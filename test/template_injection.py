from flask import Flask, render_template, requests

app = Flask(__name__)

@app.route('/')
def index():
    user_input = requests.args.get('input', 'default_value')
    # Vulnerable template string using format()
    template = 'Hello, {}!'.format(user_input)
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True)

