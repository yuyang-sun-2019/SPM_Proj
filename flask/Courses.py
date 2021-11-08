from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:spmdb123@spmdb1.c4n4efeq3vyp.us-east-1.rds.amazonaws.com:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Course(db.Model):
    __tablename__ = 'course_details'

    course_id = db.Column(db.String(50), primary_key=True)
    course_name = db.Column(db.String(100))
    course_type = db.Column(db.String(30))
    course_prerequisite = db.Column(db.String(64))
    course_brief = db.Column(db.String(200))
    course_class = db.Column(db.String(200))
    lessons = db.Column(db.String(64))
    start_date = db.Column(db.DateTime(30))
    end_date = db.Column(db.DateTime(30))

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
    



class Course_Class(db.Model):
    __tablename__ = 'course_class'

    course_class_id = db.Column(db.String(20), primary_key=True)
    course_id = db.Column(db.String(20))
    seats_available = db.Column(db.Integer)
    

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
    
 



class Course_Lesson(db.Model):
    __tablename__ = 'course_lesson'

    course_lesson_id = db.Column(db.String(20), primary_key=True)
    course_id = db.Column(db.String(20))
    pdf_material = db.Column(db.String(300))
    ppt_material = db.Column(db.String(300))
    video_material = db.Column(db.String(300))
    doc_material = db.Column(db.String(300))
    quiz_id = db.Column(db.String(20))
    

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
    
 


class Course_Progress(db.Model):
    __tablename__ = 'progress'

    progress_id = db.Column(db.String(64), primary_key=True)
    engineer_id = db.Column(db.Integer())
    course_id = db.Column(db.String(300))
    lesson = db.Column(db.String(300))
    pdf_material = db.Column(db.String(300))
    ppt_material = db.Column(db.String(300))
    video_material = db.Column(db.String(300))
    doc_material = db.Column(db.String(300))
    quiz_id = db.Column(db.String(20))
    

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


@app.route("/course_class")
def course_class():
    course_class_list = Course_Class.query.all()
    return jsonify(
        {
            "data": [course_class.to_dict() for course_class in course_class_list]
        }
    ), 200

@app.route("/course_class/<course_class_id>")
def course_class_by_id(course_class_id):
    course_class = Course_Class.query.filter_by(course_class_id=course_class_id).first()
    if course_class:
        return jsonify({
            "data": course_class.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Course Class not found."
        }), 404



@app.route("/course_lesson")
def course_lesson():
    course_lesson_list = Course_Lesson.query.all()
    return jsonify(
        {
            "data": [course_lesson.to_dict() for course_lesson in course_lesson_list]
        }
    ), 200

@app.route("/course_lesson/<course_lesson_id>")
def course_lesson_by_id(course_lesson_id):
    course_lesson = Course_Lesson.query.filter_by(course_lesson_id=course_lesson_id).first()
    if course_lesson:
        return jsonify({
            "data": course_lesson.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Course Lesson not found."
        }), 404

@app.route("/course_progress/<progress_id>")
def courses_progress(progress_id):
    course_progress = Course_Progress.query.filter_by(progress_id=progress_id).first()
    if course_progress:
        return jsonify({
            "data": course_progress.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Course progress not found."
        }), 404
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
