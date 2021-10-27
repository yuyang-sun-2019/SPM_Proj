from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root' + \
                                        '@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app, origins= "http://localhost")



class Course(db.Model):
    __tablename__ = 'course_details'

    course_id = db.Column(db.String(50), primary_key=True)
    course_name = db.Column(db.String(100))
    course_prerequisite = db.Column(db.String(64))
    course_type = db.Column(db.String(30))
    course_brief = db.Column(db.String(200))
    total_slots_available = db.Column(db.Integer)
    course_period = db.Column(db.String(64))
    FK_trainer_course_section_id = db.Column(db.String(200))
    FK_quiz_id = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_identity': 'course_details'
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
    
    def get_CourseID(self):
        return self.course_id
    
    def get_CourseName(self):
        return self.course_name
    
    def get_CourseType(self):
        return self.course_type
    
    def get_CoursePrerequisite(self):
        return self.course_prerequisite
    
    def get_CourseBrief(self):
        return self.course_brief
    
    def get_CourseSlotsAvail(self):
        return self.total_slots_available
    
    def get_CoursePeriod(self):
        return self.course_period
    
    def get_CourseTrainerCourseSectionID(self):
        return self.FK_trainer_course_section_id
    
    def get_CourseQuizID(self):
        return self.FK_quiz_id

db.create_all()


@app.route("/course")
def courses():
    course_list = Course.query.all()
    return jsonify(
        {
            "data": [course.to_dict() for course in course_list]
        }
    ), 200

@app.route("/course/<course_id>")
def course_by_id(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        return jsonify({
            "data": course.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404


@app.route("/course_prereq/<course_id>")
def coursePrereq_by_id(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        return jsonify({
            "Prequisites for Course": course.get_CoursePrerequisite()
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404

@app.route("/course_descr/<course_id>")
def courseDescr_by_id(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        return jsonify({
            "Prequisites for Course": course.get_CourseBrief()
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)