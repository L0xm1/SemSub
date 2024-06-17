from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store vulnerabilities
vulnerabilities = []

@app.route('/')
def index():
    return render_template('index.html', vulnerabilities=vulnerabilities)

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    
    vulnerabilities.append(data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
