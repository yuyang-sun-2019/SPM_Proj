from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@MySQL:3306/g7-6_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Quiz:
    __tablename__ = 'quiz'
    def __init__(self, quiz_id='', quiz_title='',
                 quiz_score='',
                 quiz_start_datetime='', quiz_end_datetime='', quiz_content=''):
        self.quiz_id = quiz_id
        self.quiz_title = quiz_title
        self.quiz_score = quiz_score
        self.quiz_start_datetime = quiz_start_datetime
        self.quiz_end_datetime = quiz_end_datetime
        self.quiz_content = quiz_content

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

class Quiz_qn:
    __tablename__ = 'quiz_qn'
    def __init__(self, qn_id='', quiz_id='',
                 qn_score='',
                 qn_content=''):
        self.qn_id = qn_id
        self.quiz_id = quiz_id
        self.qn_score = qn_score
        self.qn_content = qn_content

    def get_qn_id(self):
        return self.qn_id
    
    def get_quiz_id(self):
        return self.quiz_id
    
    def get_qn_score(self):
        return self.qn_score
    
    def get_qn_content(self):
        return self.qn_content

class Ans_key:
    __tablename__ = 'quiz_qn'
    def __init__(self, ans_id='', quiz_id='',
                 qn_id='',
                 correct='', ans_key='' ):
        self.ans_id = ans_id
        self.quiz_id = quiz_id
        self.qn_id = qn_id
        self.correct = correct
        self.ans_key = ans_key

    def get_ans_id(self):
        return self.ans_id
    
    def get_quiz_id(self):
        return self.quiz_id
    
    def get_qn_id(self):
        return self.qn_id
    
    def get_correct(self):
        return self.correct

    def get_ans_key(self):
        return self.ans_key

class Take_table:
    __tablename__ = 'Take_table'
    def __init__(self, take_id='', engineer_id='',
                 quiz_id='',
                 engineer_score='', startedAt='', finishedAt='' ):
        self.take_id = take_id
        self.engineer_id = engineer_id
        self.quiz_id = quiz_id
        self.engineer_score = engineer_score
        self.startedAt = startedAt
        self.finishedAt = finishedAt

    def get_take_id(self):
        return self.take_id
    
    def get_engineer_id(self):
        return self.engineer_id
    
    def get_quiz_id(self):
        return self.quiz_id
    
    def get_engineer_score(self):
        return self.engineer_score

    def get_startedAt(self):
        return self.startedAt

class Take_ans:
    __tablename__ = 'take_ans'
    def __init__(self, take_ans_id='',take_id='',
                 qn_id='',
                 ans_id=''):
        self.take_ans_id = take_ans_id
        self.take_id = take_id
        self.qn_id = qn_id
        self.ans_id = ans_id
    
    def get_take_ans_id(self):
        return self.take_ans_id
    
    def get_take_id(self):
        return self.take_id
    
    def get_qn_id(self):
        return self.qn_id

    def get_ans_id(self):
        return self.ans_id

# s1 = Student()

# s1.name = 'Vedant'
# s1.date_of_birth = datetime(1998, 8, 8)
# s1.nric = 'ABCDEFG88'

# print(s1.get_name())
# print(s1.get_age())
# print(s1.nric)
