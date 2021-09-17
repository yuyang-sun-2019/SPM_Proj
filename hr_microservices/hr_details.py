from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/HRs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

#HR` (`HR_ID`, `HR_Name`, `HR_password`) VALUES
 
class HRs(db.Model):
    __tablename__ = 'HRs'
 
    HR_ID = db.Column(db.Integer, primary_key=True)
    HR_Name = db.Column(db.String(64), nullable=False)
    HR_password = db.Column(db.String(64), nullable=False)
    
   
    def __init__(self, HR_ID,HR_Name,HR_password):
        self.HR_ID = HR_ID
        self.HR_Name = HR_Name
        self.HR_password = HR_password
 
    def json(self):
        return {
            'HR_ID':self.HR_ID,
            'HR_Name': self.HR_Name,
            'HR_password': self.HR_password,
        }

 
@app.route("/HRs")
def get_all_HRs():
    HR_list = HRs.query.all()
    if len(HR_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "HRs": [HRs_all.json() for HRs_all in HR_list]
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
    app.run(port=5004, debug=True)


