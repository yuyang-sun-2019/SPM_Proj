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
    engineer_id= db.Column(db.String(100))
    course_id = db.Column(db.String(200))

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
    
    def get_enrollment_ID(self):
        return self.enrollment_id
    
    def get_user_id(self):
        return self.engineer_id
    
    def get_course_id(self):
        return self.course_id

db.create_all()



# @app.route("/enrollment", methods=['POST'])
# def create_enrollment():
#     data = request.get_json()
#     if not all(key in data.keys() for
#                key in ('user_id', 'course_id')):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500
    
#     # # (1): Validate course_id
#     # course_id = Course.query.filter_by(course_id=data['course_id']).first()
#     # if not course_id:
#     #     return jsonify({
#     #         "message": "Course not valid."
#     #     }), 500

#     # # (3): Validate engineer_id
#     # user_id = Engineers.query.filter_by(user_id=data['user_id']).first()
#     # if not user_id:
#     #     return jsonify({
#     #         "message": "Engineer not valid."
#     #     }), 500

#     # # (4): Create enrollment record
#     enrollment= Enrollment(
#         course_id=data['course_id'], user_id=data['user_id'])
    
#     # # (5): Commit to DB
#     try:
#         db.session.add(enrollment)
#         db.session.commit()
#         return jsonify(enrollment.to_dict()), 201
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }), 500


@app.route("/enrollment", methods=['POST'])
def create_enrollment():
    data = request.get_json()
    # print(data)
    if not all(key in data.keys() for
               key in ('engineer_id', 'course_id')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    enrollment = Enrollment(
      engineer_id=data['engineer_id'], course_id=data['course_id'])
    print(enrollment.get_course_id())
    print(enrollment.get_user_id())
    print(enrollment.get_enrollment_ID())
    # print(enrollment.user_id)
    # print(enrollment.course_id)

    try:
        db.session.add(enrollment)
        db.session.commit()
        return jsonify(enrollment.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# @app.route("/enrollment/<string:course_id>")
# def find_by_id(course_id):
#     course_id = Course.query.filter_by(course_id=course_id).first()
#     if course_id:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": course_id.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Course ID not found."
#         }
#     ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)