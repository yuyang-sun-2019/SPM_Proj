import unittest

from Quiz import Quiz, quiz_qn_ans


# Done by Ho Jing Ling
class TestQuiz(unittest.TestCase):
    c1 = Quiz(quiz_id='C101-L1-Quiz', quiz_title='C101-L1', quiz_duration='00:15:00', FK_trainer_id='761')
    def test_to_dict(self):
        self.assertEqual(self.c1.to_dict(), {
            'quiz_id': 'C101-L1-Quiz',
            'quiz_title': 'C101-L1',
            'quiz_duration': '00:15:00',
            'FK_trainer_id': '761'
        }
        )

# # Done by Ho Jing Ling
class Testquiz_qn_ans(unittest.TestCase):
    cc1 = quiz_qn_ans(quiz_qn_id='MCQ_Qn1')
    def test_to_dict(self):
        self.assertTrue(self.cc1.to_dict(), {
            'quiz_qn_id': 'MCQ_Qn1',
            'quiz_qn_id': 'MCQ_Qn1_A',
            'quiz_qn_id': 'MCQ_Qn1_B',
            'quiz_qn_id': 'MCQ_Qn1_C',
            'quiz_qn_id': 'MCQ_Qn1_D',
            'quiz_qn_id': 'MCQ_Qn1_Ans',
            'quiz_qn_id': 'MCQ_Qn1_Score',
            'quiz_qn_id': 'MCQ_Qn2',
            'quiz_qn_id': 'MCQ_Qn2_A',
            'quiz_qn_id': 'MCQ_Qn2_B',
            'quiz_qn_id': 'MCQ_Qn2_C',
            'quiz_qn_id': 'MCQ_Qn2_D',
            'quiz_qn_id': 'MCQ_Qn2_Ans',
            'quiz_qn_id': 'MCQ_Qn2_Score',
            'quiz_qn_id': 'TandF_Qn1',
            'quiz_qn_id': 'TandF_Qn1_Ans',
            'quiz_qn_id': 'TandF_Qn1_Score',            
            'quiz_qn_id': 'TandF_Qn2',
            'quiz_qn_id': 'TandF_Qn2_Ans',
            'quiz_qn_id': 'TandF_Qn2_Score'            

        }
        )

if __name__ == '__main__':
    unittest.main()