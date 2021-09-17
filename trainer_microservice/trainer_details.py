from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/trainers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

# Trainers` (`trainerID`, `trainerName`, `trainer_teleID`, `trainer_emailID`,'trainer_courses') VALUES
 
class trainers(db.Model):
    __tablename__ = 'trainers'
 
    trainerID = db.Column(db.Integer, primary_key=True)
    trainerName = db.Column(db.String(64), nullable=False)
    trainer_teleID = db.Column(db.String(64), nullable=False)
    trainer_emailID = db.Column(db.String(64), nullable=False)
    trainer_courses = db.Column(db.String(64), nullable=False)
   
    def __init__(self, trainerID,trainerName,trainer_teleID,trainer_emailID,trainer_courses):
        self.trainerID = trainerID
        self.trainerName = trainerName
        self.trainer_teleID = trainer_teleID
        self.trainer_emailID = trainer_emailID
        self.trainer_courses = trainer_courses
 
    def json(self):
        return {
            'trainerID':self.trainerID,
            'trainerName': self.trainerName,
            'trainer_teleID': self.trainer_teleID,
            'trainer_emailID': self.trainer_emailID,
            'trainer_courses':self.trainer_courses
        
        }

 
@app.route("/trainers")
def get_all_trainers():
    trainerlist = trainers.query.all()
    if len(trainerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Trainers": [trainers.json() for trainers in trainerlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Trainers not found."
        }
    ), 404

 

 
# @app.route("/book/<string:isbn13>")
# def find_by_isbn13(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if book:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": book.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Book not found."
#         }
#     ), 404



 
# @app.route("/book/<string:isbn13>", methods=['POST'])
# def create_book(isbn13):
#     if (Book.query.filter_by(isbn13=isbn13).first()):
#         return jsonify(
#             {
#                 "code": 400,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "Book already exists."
#             }
#         ), 400
 
#     data = request.get_json()
#     book = Book(isbn13, **data)
 
#     try:
#         db.session.add(book)
#         db.session.commit()
#     except:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "An error occurred creating the book."
#             }
#         ), 500
 
#     return jsonify(
#         {
#             "code": 201,
#             "data": book.json()
#         }
#     ), 201



 
if __name__ == '__main__':
    app.run(port=5003, debug=True)


