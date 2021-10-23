from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''' + \
                                        '@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Person(db.Model):
    __tablename__ = 'Person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    pwd = db.Column(db.String(80))

    def __init__(self,id,name,email,pwd):
        self.id = id
        self.name: name
        self.email: email
        self.pwd:pwd

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'pwd': self.pwd
        }


@app.route("/person")
def get_all_person():
    people = Person.query.all()
    if len(people):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Person": [person.json() for person in people]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Person not found."
        }
    ), 404


@app.route("/person/<string:id>")
def find_by_id(id):
    person = Person.query.filter_by(id=id).first()
    if person:
        return jsonify(
            {
                "code": 200,
                "data": person.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Person ID not found."
        }
    ), 404


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) +
          ": manage person details ...")
    app.run(host='0.0.0.0', port=5001, debug=True)