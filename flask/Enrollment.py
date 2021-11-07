from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from Person import *
from Courses import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''' + \
                                        '@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Enrollment(db.Model):
    __tablename__ = 'enrollment'

    enrollment_id = db.Column(db.Integer, primary_key=True)
    engineer_id= db.Column(db.Integer)
    course_id = db.Column(db.String(20))
    course_class_id = db.Column(db.String(20))

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
    
   

db.create_all()

@app.route("/enrollment")
def get_enrolllment():
    enrollment_list = Enrollment.query.all()
    return jsonify(
        {
            "data": [enrolllment.to_dict() for enrolllment in enrollment_list]
        }
    ), 200


@app.route("/enrollment", methods=['POST'])
def create_enrollment():
    data = request.get_json()
    # print(data)
    if not all(key in data.keys() for
               key in ('engineer_id', 'course_id', 'course_class_id')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    enrollment = Enrollment(
      engineer_id=data['engineer_id'], course_id=data['course_id'], course_class_id=data['course_class_id'])

    

    try:
        db.session.add(enrollment)
        db.session.commit()
        return jsonify(enrollment.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
