# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Store dialed numbers
dialed_numbers = []

@app.route('/dial', methods=['POST'])
def dial():
    number = request.json.get('number')
    if number:
        dialed_numbers.append(number)
        return jsonify({"message": "Number dialed", "dialed_numbers": dialed_numbers}), 200
    return jsonify({"error": "No number provided"}), 400

@app.route('/dialed_numbers', methods=['GET'])
def get_dialed_numbers():
    return jsonify({"dialed_numbers": dialed_numbers})

if __name__ == '__main__':
    app.run(debug=True)
