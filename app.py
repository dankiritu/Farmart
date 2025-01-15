from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://farmart_user:yourpassword@localhost/farmart'
db = SQLAlchemy(app)

# Define your models (e.g., Animal, User)
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)

@app.route('/animals', methods=['GET'])
def get_animals():
    animals = Animal.query.all()
    return jsonify([animal.name for animal in animals])

if __name__ == '__main__':
    app.run(debug=True)
