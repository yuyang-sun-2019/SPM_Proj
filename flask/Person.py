from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

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
    name = db.Column(db.String(15))
    email = db.Column(db.String(50), unique=True)
    pwd = db.Column(db.String(80), unique=True)

    __mapper_args__ = {
        'polymorphic_identity': 'person'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Engineer(db.Model):
    __tablename__ = 'engineers'

    engineer_id = db.Column(db.Integer, primary_key=True)
    engineer_teleid = db.Column(db.String(20))
    engineer_completed_coursesid = db.Column(db.String(64))
    engineer_inprogress_coursesid = db.Column(db.String(64))
    engineer_preassigned_coursesid = db.Column(db.String(64))
    engineer_biddable_coursesid = db.Column(db.String(64))


    __mapper_args__ = {
        'polymorphic_identity': 'engineers'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result



@app.route("/person")
def get_all_person():
    people = Person.query.all()
    if len(people):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Person": [person.to_dict() for person in people]
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
                "data": person.to_dict()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Person ID not found."
        }
    ), 404


@app.route("/engineer")
def get_all_engineer():
    engineers = Engineer.query.all()
    if len(engineers):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Person": [eng.to_dict() for eng in engineers]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Engineer not found."
        }
    ), 404

@app.route("/engineer/<string:engineer_id>")
def get_engineer_byID(engineer_id):
    engineer = Engineer.query.filter_by(engineer_id=engineer_id).first()
    if engineer:
        return jsonify(
            {
                "code": 200,
                "data": engineer.to_dict()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Engineer not found."
        }
    ), 404




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)