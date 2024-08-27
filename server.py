# app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dialed_numbers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model
class DialedNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<DialedNumber {self.number}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/dial', methods=['POST'])
def dial():
    number = request.json.get('number')
    if number:
        new_number = DialedNumber(number=number)
        db.session.add(new_number)
        db.session.commit()
        return jsonify({"message": "Number dialed", "dialed_numbers": [n.number for n in DialedNumber.query.all()]}), 200
    return jsonify({"error": "No number provided"}), 400

@app.route('/dialed_numbers', methods=['GET'])
def get_dialed_numbers():
    numbers = [n.number for n in DialedNumber.query.all()]
    return jsonify({"dialed_numbers": numbers})

if __name__ == '__main__':
    app.run(debug=True)
