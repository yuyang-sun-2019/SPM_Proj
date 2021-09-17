from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/engineers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)
 
class Engineers(db.Model):
    __tablename__ = 'engineers'

    engineer_id = db.Column(db.Integer, primary_key=True)
    engineer_pwd = db.Column(db.String(10))
    engineer_name = db.Column(db.String(64))
    engineer_teleid = db.Column(db.String(20))
    engineer_email = db.Column(db.String(20))
    engineer_completedCourses = db.Column(db.String)
    engineer_enrolledCourses = db.Column(db.String)
    engineer_assignedCourses = db.Column(db.String)
    engineer_signedupCourses = db.Column(db.String)

    def __init__(self, engineer_id, engineer_pwd, engineer_name, engineer_teleid, engineer_email, engineer_completedCourses, engineer_enrolledCourses, engineer_assignedCourses, engineer_signedupCourses):
        self.engineer_id = engineer_id
        self.engineer_pwd = engineer_pwd
        self.engineer_name = engineer_name
        self.engineer_teleid = engineer_teleid
        self.engineer_email = engineer_email
        self.engineer_completedCourses = engineer_completedCourses
        self.engineer_erolledCourses = engineer_enrolledCourses
        self.engineer_assignedCourses = engineer_assignedCourses
        self.engineer_signedupCourses = engineer_signedupCourses

    def json(self):
        return {"engineer_id": self.engineer_id, "engineer_pwd": self.engineer_pwd, "engineer_name": self.engineer_name, "engineer_teleid": self.engineer_teleid, "engineer_email": self.engineer_email, "engineer_completedCourses": self.engineer_completedCourses, "engineer_enrolledCourses": self.engineer_enrolledCourses, "engineer_assignedCourses": self.engineer_assignedCourses, "engineer_signedupCourses": self.engineer_signedupCourses}


@app.route("/engineers")
def get_all():
    engineers_list = Engineers.query.all()
    if len(engineers_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "engineers_list": [engineers.json() for engineers in engineers_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Engineers List Unavailable."
        }
    ), 404


@app.route("/engineers/<string:engineer_id>")
def find_by_engineer_id(engineer_id):
    engineer = Engineers.query.filter_by(engineer_id=engineer_id).first()
    if engineer:
        return jsonify(
            {
                "code": 200,
                "data": engineer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Engineer is not registered in the System."
        }
    ), 404


@app.route("/engineers/<string:engineer_id>", methods=['POST'])
def create_engineer(engineer_id):
    if (Engineers.query.filter_by(engineer_id=engineer_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "engineer_id": engineer_id
                },
                "message": "Engineer is already registered in the System."
            }
        ), 400

    data = request.get_json()
    engineer = Engineers(engineer_id, **data)

    try:
        db.session.add(engineer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "engineer_id": engineer_id
                },
                "message": "An error occurred while registering the Engineer. Sorry!"
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": engineer.json()
        }
    ), 201


@app.route("/engineers/<string:engineer_id>", methods=['DELETE'])
def delete_engineer(engineer_id):
    engineer = Engineers.query.filter_by(engineer_id=engineer_id).first()
    if engineer:
        db.session.delete(engineer)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "engineer_id": engineer_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "engineer_id": engineer_id
            },
            "message": "Engineer is not found in our System."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)