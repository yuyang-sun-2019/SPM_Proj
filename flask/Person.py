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
    engineer_completed_courses = db.Column(db.String(64))
    engineer_inprogress_courses = db.Column(db.String(64))


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


class Trainers(db.Model):
    __tablename__ = 'trainers'

    trainer_id = db.Column(db.Integer, primary_key=True)
    trainer_course_class_id= db.Column(db.String(200))

    __mapper_args__ = {
        'polymorphic_identity': 'enrollment'
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
    
    def get_trainer_id(self):
        return self.trainer_id
    
    def get_trainer_course_class_id(self):
        return self.trainer_course_class_id



class HR(db.Model):
    __tablename__ = 'hr'

    hr_id = db.Column(db.Integer, primary_key=True)
    courses_assigned= db.Column(db.String(200))

    __mapper_args__ = {
        'polymorphic_identity': 'hr'
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
    
    def get_hr_id(self):
        return self.trainer_id
    
    def get_courses_assigned(self):
        return self.courses_assigned




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


@app.route("/trainer")
def trainers():
    trainer_list = Trainers.query.all()
    return jsonify(
        {
            "data": [trainer.to_dict() for trainer in trainer_list]
        }
    ), 200

@app.route("/trainer/<trainer_id>")
def trainer_by_id(trainer_id):
    trainer_course_class_list = Trainers.query.filter_by(trainer_id=trainer_id).first()
    if trainer_course_class_list:
        return jsonify({
            "data": trainer_course_class_list.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Trainer not found."
        }), 404



@app.route("/hr")
def hr():
    hr_list = HR.query.all()
    return jsonify(
        {
            "data": [hr.to_dict() for hr in hr_list]
        }
    ), 200

@app.route("/hr/<hr_id>")
def hr_by_id(hr_id):
    hr_course_list = HR.query.filter_by(hr_id=hr_id).first()
    if hr_course_list:
        return jsonify({
            "data": hr_course_list.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "HR not found."
        }), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
