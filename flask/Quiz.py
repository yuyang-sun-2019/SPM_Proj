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


class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.String(75), primary_key=True)
    quiz_title= db.Column(db.String(100))
    quiz_duration = db.Column(db.String(30))
    FK_trainer_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'quiz'
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


@app.route("/quiz")
def quiz():
    quiz_list = Quiz.query.all()
    return jsonify(
        {
            "data": [quiz.to_dict() for quiz in quiz_list]
        }
    ), 200

@app.route("/quiz/<quiz_id>")
def quiz_by_id(quiz_id):
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()
    if quiz:
        return jsonify({
            "data": quiz.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Quiz not found."
        }), 404
"''''"



@app.route("/quiz", methods=['POST'])
def create_quiz():
    data = request.get_json()
    # print(data)
    if not all(key in data.keys() for
               key in ('quiz_id', 'quiz_title', 'quiz_duration','FK_trainer_id')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    quiz_description = Quiz(
      quiz_id=data['quiz_id'], quiz_title=data['quiz_title'],quiz_duration=data['quiz_duration'], FK_trainer_id=data['FK_trainer_id'] )

    try:
        db.session.add(quiz_description)
        db.session.commit()
        return jsonify(quiz_description.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500






class quiz_qn_ans(db.Model):
    __tablename__ = 'quiz_qn_ans'

    quiz_qn_id = db.Column(db.String(75), primary_key=True)

    MCQ_Qn1 =db.Column(db.String(75))
    MCQ_Qn1_A =db.Column(db.String(75))
    MCQ_Qn1_B =db.Column(db.String(75))
    MCQ_Qn1_C =db.Column(db.String(75))
    MCQ_Qn1_D =db.Column(db.String(75))
    MCQ_Qn1_Ans =db.Column(db.String(75))
    MCQ_Qn1_Score =db.Column(db.Integer)

    MCQ_Qn2 =db.Column(db.String(75))
    MCQ_Qn2_A =db.Column(db.String(75))
    MCQ_Qn2_B =db.Column(db.String(75))
    MCQ_Qn2_C =db.Column(db.String(75))
    MCQ_Qn2_D =db.Column(db.String(75))
    MCQ_Qn2_Ans =db.Column(db.String(75))
    MCQ_Qn2_Score =db.Column(db.Integer)

    TandF_Qn1 =db.Column(db.String(75))
    TandF_Qn1_Ans =db.Column(db.String(75))
    TandF_Qn1_Score =db.Column(db.Integer)

    TandF_Qn2 =db.Column(db.String(75))
    TandF_Qn2_Ans =db.Column(db.String(75))
    TandF_Qn2_Score =db.Column(db.Integer)


    __mapper_args__ = {
        'polymorphic_identity': 'quiz_qn_ans'
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


@app.route("/quiz_qn_ans")
def quiz_qn():
    quiz_qn_list = quiz_qn_ans.query.all()
    return jsonify(
        {
            "data": [quiz_qn.to_dict() for quiz_qn in quiz_qn_list]
        }
    ), 200

@app.route("/quiz_qn_ans/<quiz_qn_id>")
def quiz_qn_by_id(quiz_qn_id):
    quiz = quiz_qn_ans.query.filter_by(quiz_qn_id=quiz_qn_id).first()
    if quiz:
        return jsonify({
            "data": quiz.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Quiz not found."
        }), 404




@app.route("/quiz_question_ans", methods=['POST'])
def create_quiz_qn():
    data = request.get_json()
    # print(data)
    if not all(key in data.keys() for
               key in (
    'quiz_qn_id',

    'MCQ_Qn1' ,
    'MCQ_Qn1_A',
    'MCQ_Qn1_B', 
    'MCQ_Qn1_C',
    'MCQ_Qn1_D',
    'MCQ_Qn1_Ans',
    'MCQ_Qn1_Score',

    'MCQ_Qn2',
    'MCQ_Qn2_A',
    'MCQ_Qn2_B',
    'MCQ_Qn2_C',
    'MCQ_Qn2_D',
    'MCQ_Qn2_Ans',
    'MCQ_Qn2_Score',

    'TandF_Qn1',
    'TandF_Qn1_Ans',
    'TandF_Qn1_Score',

    'TandF_Qn2',
    'TandF_Qn2_Ans',
    'TandF_Qn2_Score'
)):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    quiz_question = quiz_qn_ans(
      
   quiz_qn_id =data['quiz_qn_id'],
   MCQ_Qn1= data['MCQ_Qn1'],
   MCQ_Qn1_A= data['MCQ_Qn1_A'] ,
   MCQ_Qn1_B= data['MCQ_Qn1_B'], 
   MCQ_Qn1_C= data['MCQ_Qn1_C'],
   MCQ_Qn1_D= data['MCQ_Qn1_D'],
   MCQ_Qn1_Ans= data['MCQ_Qn1_Ans'],
   MCQ_Qn1_Score= data['MCQ_Qn1_Score'],

   MCQ_Qn2= data['MCQ_Qn2'],
   MCQ_Qn2_A= data['MCQ_Qn2_A'],
   MCQ_Qn2_B=data['MCQ_Qn2_B'],
   MCQ_Qn2_C= data['MCQ_Qn2_C'],
   MCQ_Qn2_D= data['MCQ_Qn2_D'],
   MCQ_Qn2_Ans= data['MCQ_Qn2_Ans'],
   MCQ_Qn2_Score= data['MCQ_Qn2_Score'],

   TandF_Qn1= data['TandF_Qn1'],
   TandF_Qn1_Ans= data['TandF_Qn1_Ans'],
   TandF_Qn1_Score= data['TandF_Qn1_Score'],

   TandF_Qn2=data['TandF_Qn2'],
   TandF_Qn2_Ans= data['TandF_Qn2_Ans'],
   TandF_Qn2_Score=data['TandF_Qn2_Score']
)

    try:
        db.session.add(quiz_question)
        db.session.commit()
        return jsonify(quiz_question.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500



class quiz_take(db.Model):
    __tablename__ = 'quiz_take'

    quiz_take_id = db.Column(db.String(75), primary_key=True)
    quiz_score = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'quiz'
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

    def get_quiz_take_id(self):
        return self.quiz_take_id
    
    def get_quiz_score(self):
        return self.quiz_score



db.create_all()


@app.route("/quiz_take")
def quiz_taken():
    quiz_take_list = quiz_take.query.all()
    return jsonify(
        {
            "data": [quiz.to_dict() for quiz in quiz_take_list]
        }
    ), 200

@app.route("/quiz_take/<quiz_take_id>")
def quiz_take_by_id(quiz_take_id):
    quiz_taken = quiz_take.query.filter_by(quiz_take_id=quiz_take_id).first()
    if quiz:
        return jsonify({
            "data": quiz_taken.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Quiz not found."
        }), 404
"''''"



@app.route("/quiz_take", methods=['POST'])
def create_quiz_take():
    data = request.get_json()
    print(data)
    if not all(key in data.keys() for
               key in ('quiz_take_id', 'quiz_score')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    quizzes_taken = quiz_take(
      quiz_take_id=data['quiz_take_id'], quiz_score=data['quiz_score'] )
    

    try:
        db.session.add(quizzes_taken)
        db.session.commit()
        return jsonify(quizzes_taken.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
