import unittest

import unittest

from Quiz import Quiz, quiz_qn_ans, quiz_take 

###Done by Ho Jing Ling
##Test if there is a quiz 
class TestQuiz(unittest.TestCase):
    q1 = Quiz(quiz_id='C101-L1-Quiz', quiz_title='C101-L1', quiz_duration ='00:15:00', FK_trainer_id= '761')
    
    
    def test_to_dict(self):
        self.assertEqual(self. q1.to_dict(), {
            'quiz_id': 'C101-L1-Quiz',
            'quiz_title': 'C101-L1',
            'quiz_duration': '00:15:00',
            'FK_trainer_id' : '761',
        }
        )

    # Check if the Quiz Id is in the correct format
    def test_quiz_id(self):
        self.assertIn(self.q1.to_dict()['quiz_id'].split('-')[2][0], 'Q')


## Test for the presence of quiz_qn_as
class Testquiz_qn_ans(unittest.TestCase):
    cc1 = quiz_qn_ans(quiz_qn_id='C101-L1-Quiz',  
            MCQ_Qn1= 'What is the  lesson?',
            MCQ_Qn1_A='SPM',
            MCQ_Qn1_B='ESM', 
            MCQ_Qn1_C='ESD', 
            MCQ_Qn1_D='SPM', 
            MCQ_Qn1_Ans='1', 
            MCQ_Qn1_Score='1', 
            MCQ_Qn2='What is the most favourite color?', 
            MCQ_Qn2_A='red', 
            MCQ_Qn2_B='pink', 
            MCQ_Qn2_C='yellow', 
            MCQ_Qn2_D='blue', 
            MCQ_Qn2_Ans='blue', 
            MCQ_Qn2_Score='1', 
            TandF_Qn1='I like starbucks?', 
            TandF_Qn1_Ans='True', 
            TandF_Qn1_Score='1', 
            TandF_Qn2='I do not like strabucks?',
            TandF_Qn2_Ans='False',
            TandF_Qn2_Score='1'
)
    def test_to_dict(self):
        self.assertEqual(self.cc1.to_dict(), {
            
            'quiz_qn_id': 'C101-L1-Quiz',
            'MCQ_Qn1': 'What is the  lesson?',
            'MCQ_Qn1_A':'SPM',
            'MCQ_Qn1_B':'ESM', 
            'MCQ_Qn1_C':'ESD', 
            'MCQ_Qn1_D':'SPM', 
            'MCQ_Qn1_Ans':'1', 
            'MCQ_Qn1_Score':'1', 
            'MCQ_Qn2':'What is the most favourite color?', 'MCQ_Qn2_A':'red', 
            'MCQ_Qn2_B':'pink', 
            'MCQ_Qn2_C':'yellow', 
            'MCQ_Qn2_D':'blue', 
            'MCQ_Qn2_Ans':'blue', 
            'MCQ_Qn2_Score':'1', 
            'TandF_Qn1':'I like starbucks?', 
            'TandF_Qn1_Ans':'True', 
            'TandF_Qn1_Score':'1', 
            'TandF_Qn2':'I do not like strabucks?', 
            'TandF_Qn2_Ans':'False',
            'TandF_Qn2_Score':'1'

        }
        )
        
class TestQuizTake(unittest.TestCase):
    t1 = quiz_take(quiz_take_id='001-C101-L1', quiz_score=2)
    
    
    def test_to_dict(self):
        self.assertEqual(self.t1.to_dict(), {
            'quiz_take_id': '001-C101-L1',
            'quiz_score': 2,
        }
        )

  # Test scores are greater or equal to 0
    def test_q_score(self):
        self.assertGreater(self.t1.to_dict()['quiz_score'], -1)

    # Check if the quiz_take_id is in the correct format
    def test_quiz_id(self):
        self.assertIn(self.t1.to_dict()['quiz_take_id'].split('-')[2][0], 'L')

    

if __name__ == '__main__':
    unittest.main()   
