from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/coursedetails'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# D: Course details - list of courses/prerequisites ,  {CourseID, CourseName, CoursePrerequisite, CourseBrief, SlotsAvailable, 
# CoursePeriod, SectionID}

db = SQLAlchemy(app)

# CourseID, CourseName, CoursePrerequisite, CourseBrief, SlotsAvailable, CoursePeriod, SectionID

class CourseDetails(db.Model):
    __tablename__ = 'course_details'

    course_id = db.Column(db.Integer, primary_key = True)
    course_name = db.Column(db.String(64), nullable=False)
    course_prerequisite = db.Column(db.String(100), nullable=False)
    course_brief = db.Column(db.String(300), nullable=False)
    slots_available = db.Column(db.Integer, nullable=False)
    course_period = db.Column(db.Integer)
    section_id = db.Column(db.Integer)

    # def __init__(self, tradesman_id, name, phone_no, email, address, rating):
        # self.tradesman_id = tradesman_id
        # self.name = name
        # self.phone_no = phone_no
        # self.email = email
        # self.address = address
        # self.rating = rating

    def __init__(self, course_id, course_name, course_prerequisite, course_brief, slots_available, course_period, section_id):
        self.course_id = course_id
        self.course_name = course_name
        self.course_prerequisite = course_prerequisite
        self.course_brief = course_brief
        self.slots_available = slots_available
        self.course_period = course_period
        self.section_id = section_id

    def json(self):
        return {
            'course_id' : self.course_id, 
            "course_name" : self.course_name, 
            'course_prerequisite' : self.course_prerequisite,
            'course_brief' : self.course_brief,
            'slots_available': self.slots_available,
            'course_period': self.course_period,
            'section_id': self.section_id
        }


# GET ALL course details
@app.route("/course_details" , methods = ['GET'])
def get_all():
    course_details_list = CourseDetails.query.all()
    if len(course_details_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_details": [course_details.json() for course_details in course_details_list]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "Course Details Unavailable."
        }
    ), 404

# FIND COURSE BY ID
@app.route("/course_details/<string:course_id>")
def find_by_course_id(course_id):
    course_detail = CourseDetails.query.filter_by(course_id=course_id).first()
    if course_detail:
        return jsonify(
            {
                "code": 200,
                "data": course_detail.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "Course is not registered."
        }
    ), 404

# CREATE COURSE
@app.route("/course_details/<string:course_id>", methods=['POST'])
def create_course(course_id):
    if (CourseDetails.query.filter_by(course_id=course_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "course_id": course_id
                },
                "message": "Course is already registered in the System."
            }
        ), 400

    data = request.get_json()
    course_details = CourseDetails(course_id, **data)

    try:
        db.session.add(course_details)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "course_id": course_id
                },
                "message": "An error occurred while registering the Course. Sorry!"
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": course_details.json()
        }
    ), 201

# DELETE COURSE BY ID
@app.route("/course_details/<string:course_id>", methods=['DELETE'])
def delete_course(course_id):
    course_detail = CourseDetails.query.filter_by(course_id = course_id).first()
    if course_detail:
        db.session.delete(course_detail)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_id": course_id
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "data": {
                "course_id": course_id
            },
            "message": "Course is not found."
        }
    ), 404


     
if __name__ == '__main__':
    app.run(port=5001, debug=True)
