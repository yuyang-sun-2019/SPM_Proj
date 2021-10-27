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

# CORS(app)


class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.String(75), primary_key=True)
    quiz_title= db.Column(db.String(100))
    quiz_score = db.Column(db.Integer)
    quiz_start_datetime = db.Column(db.DateTime(30))
    quiz_end_datetime = db.Column(db.DateTime(200))
    quiz_content = db.Column(db.String(150))
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
    
    def get_quiz_id(self):
        return self.quiz_id
    
    def get_quiz_title(self):
        return self.quiz_title
    
    def get_quiz_score(self):
        return self.quiz_score
    
    def get_quiz_start_datetime(self):
        return self.quiz_start_datetime
    
    def get_quiz_end_datetime(self):
        return self.quiz_end_datetime
    
    def get_quiz_content(self):
        return self.quiz_content    
    
    def get_Trainer_ID(self):
        return self.FK_trainer_id

db.create_all()


@app.route("/quiz")
def quiz():
    quiz_list = quiz.query.all()
    return jsonify(
        {
            "data": [quiz.to_dict() for quiz in quiz_list]
        }
    ), 200

@app.route("/quiz/<quiz_id>")
def quiz_by_id(quiz_id):
    quiz = quiz_by_id.query.filter_by(quiz_id=quiz_id).first()
    if quiz:
        return jsonify({
            "data": quiz.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Quiz not found."
        }), 404
"''''"

class Quiz_qn(db.Model):
    __tablename__ = 'quiz_qn'

    qn_id = db.Column(db.String(75), primary_key=True)
    qn_score = db.Column(db.Integer)
    qn_content = db.Column(db.String(150))
    FK_quiz_id = db.Column(db.String(75))

    __mapper_args__ = {
        'polymorphic_identity': 'quiz_qn'
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
    
    def get_qn_id(self):
        return self.qn_id
    
    def get_qn_score(self):
        return self.qn_score
    
    def get_qn_content(self):
        return self.qn_content
    
    def get_quiz_id(self):
        return self.FK_quiz_id



db.create_all()


# @app.route("/quiz_qn")
# def quiz_qn():
#     quiz_qn_list = quiz_qn.query.all()
#     return jsonify(
#         {
#             "data": [quiz_qn.to_dict() for quiz_qn in quiz_qn_list]
#         }
#     ), 200

# @app.route("/quiz_qn/<quiz_id>")
# def quiz_by_id(quiz_id):
#     quiz = quiz_by_id.query.filter_by(quiz_id=quiz_id).first()
#     if quiz:
#         return jsonify({
#             "data": quiz.to_dict()
#         }), 200
#     else:
#         return jsonify({
#             "message": "Quiz not found."
#         }), 404
# "''''"



class ans_key(db.Model):
    __tablename__ = 'ans_key'

    ans_id = db.Column(db.String(75), primary_key=True)
    qn_id = db.Column(db.String(75))
    correct = db.Column(db.Integer)
    ans_key = db.Column(db.Integer)
    FK_quiz_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'ans_key'
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
    
    def get_ans_id(self):
        return self.ans_id
    
    def get_qn_id(self):
        return self.quiz_id
    
    def get_correct(self):
        return self.correct
    
    def get_ans_key(self):
        return self.ans_key
 

db.create_all()


@app.route("/ans_key")
def ans_key():
    ans_key_list = ans_key.query.all()
    return jsonify(
        {
            "data": [ans_key.to_dict() for ans_key in ans_key_list]
        }
    ), 200

@app.route("/ans_key/<ans_id>")
def ans_key_id(ans_id):
    ans_id = ans_key_id.query.filter_by(ans_id=ans_id).first()
    if quiz:
        return jsonify({
            "data": ans_id.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Answer key not found."
        }), 404
"''''"



#############################
class Take_table(db.Model):
    __tablename__ = 'Take_table'

    take_id = db.Column(db.String(75), primary_key=True)
    quiz_id = db.Column(db.Integer)
    engineer_score = db.Column(db.Integer)
    startedAt = db.Column(db.DateTime(200))
    finishedAt = db.Column(db.DateTime(200))
    FK_engineer_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'take_table'
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
    
    def get_take_id(self):
        return self.take_id
    
    def get_quiz_id(self):
        return self.quiz_id
    
    def get_engineer_score(self):
        return self.quiz_score
    
    def get_startedAt(self):
        return self.quiz_start_datetime
    
    def get_quiz_end_datetime(self):
        return self.quiz_end_datetime
    
    # def get_quiz_content(self):
    #     return self.quiz_content    
    
    # def get_Trainer_ID(self):
    #     return self.FK_trainer_id

db.create_all()


@app.route("/take_table")
def take_table():
    take_table_list = take_table.query.all()
    return jsonify(
        {
            "data": [take_table.to_dict() for take_table in take_table_list]
        }
    ), 200

@app.route("/take_table/<take_id>")
def take_table_by_id(take_id):
    take_id = take_table_by_id.query.filter_by(take_id=take_id).first()
    if take_id:
        return jsonify({
            "data": take_table.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Take Table not found."
        }), 404
"''''"

########
class Take_ans(db.Model):
    __tablename__ = 'Take_ans'

    take_ans_id = db.Column(db.String(75), primary_key=True)
    FK_take_id = db.Column(db.Integer)
    FK_qn_id = db.Column(db.Integer)
    FK_ans_id = db.Column(db.Integer)


    __mapper_args__ = {
        'polymorphic_identity': 'take_ans'
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
    
    def get_take_ans_id(self):
        return self.take_ans_id

    def get_take_id(self):
        return self.take_id
    
    def get_qn_id(self):
        return self.qn_id
       
    def get_ans_id(self):
        return self.ans_id
    

db.create_all()


@app.route("/take_ans")
def take_ans():
    take_ans_list = take_ans.query.all()
    return jsonify(
        {
            "data": [take_ans.to_dict() for answers in take_ans_list]
        }
    ), 200

@app.route("/take_ans/<take_ans_id>")
def take_ans_by_id(take_ans_id):
    take_ans = take_ans_by_id.query.filter_by(take_ans_id=take_ans_id).first()
    if take_ans:
        return jsonify({
            "data": take_ans_by_id.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Answers not found."
        }), 404
"''''"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)