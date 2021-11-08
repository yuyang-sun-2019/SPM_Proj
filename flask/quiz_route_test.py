import unittest
import json

from Quiz import app, db, Quiz, quiz_qn_ans, quiz_take 


######################################################Done by Goh Xue Qi
# #################################################
# Test if API '/quiz' works
class Test_quiz(unittest.TestCase):
    # Check if response is 200
    def test_quiz(self):
        tester = app.test_client(self)
        response = tester.get("/quiz")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        
    # Check if content return is application/json
    def test_quiz(self):
        tester = app.test_client(self)
        response = tester.get("/quiz")
        self.assertEqual(response.content_type, "application/json")
        
            
    # Check if all the quiz Details requires are Present
    def test_quiz_details(self):
        tester = app.test_client(self)
        response = tester.get("/quiz")
        self.assertTrue(b'quiz_id' in response.data)
        self.assertTrue(b'quiz_title' in response.data)
        self.assertTrue(b'quiz_duration' in response.data)
        self.assertTrue(b'FK_trainer_id' in response.data)
    

## Check for Data returned
    def test_quiz_details(self):
        tester = app.test_client(self)
        response = tester.get("/quiz")
        response_body = json.loads(response.data)
        self.assertEqual('C101-L1-Quiz', response_body['data'][0]['quiz_id'])
        self.assertEqual('C101-L1', response_body['data'][0]['quiz_title'])
        self.assertEqual('00:15:00', response_body['data'][0]['quiz_duration'])
        self.assertEqual(761, response_body['data'][0]['FK_trainer_id'])



# Test if API '//quiz/quiz_id' works
class Test_quiz(unittest.TestCase):
    # Check if response is 200
    def test_quiz(self):
        tester = app.test_client(self)
        quiz_id = 'C101-L1-Quiz'
        response = tester.get("/quiz/"+quiz_id)
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_quiz(self):
        tester = app.test_client(self)
        quiz_id = 'C101-L1-Quiz'
        response = tester.get("/quiz/"+quiz_id)
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the Quiz Details requires are Present
    def test_quiz_details(self):
        tester = app.test_client(self)
        quiz_id = 'C101-L1-Quiz'
        response = tester.get("/quiz/"+quiz_id)
        self.assertTrue(b'quiz_id' in response.data)
        self.assertTrue(b'FK_trainer_id' in response.data)
        self.assertTrue(b'quiz_title' in response.data)
        self.assertTrue(b'quiz_duration' in response.data)

     
    # Check for Data returned
    def test_quiz_details(self):
        tester = app.test_client(self)
        quiz_id = 'C101-L1-Quiz'
        response = tester.get("/quiz/"+quiz_id)
        response_body = json.loads(response.data)
        self.assertEqual('C101-L1-Quiz', response_body['data']['quiz_id'])
        self.assertEqual(761, response_body['data']['FK_trainer_id'])
        self.assertEqual('C101-L1', response_body['data']['quiz_title'])
        self.assertEqual('00:15:00', response_body['data']['quiz_duration'])




################################################# Done by Goh Xue Qi #################################################
# Test if API '/quiz_qn_ans' works
class Test_quiz_qn_ans(unittest.TestCase):
    # Check if response is 200
    def test_quiz(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_qn_ans")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_quiz(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_qn_ans")
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the quiz Details requires are Present
    def test_quiz_details(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_qn_ans")
        self.assertTrue(b'quiz_qn_id' in response.data)
        self.assertTrue(b'MCQ_Qn1' in response.data)
        self.assertTrue(b'MCQ_Qn1_A' in response.data)
        self.assertTrue(b'MCQ_Qn1_B' in response.data)
        self.assertTrue(b'MCQ_Qn1_C' in response.data)
        self.assertTrue(b'MCQ_Qn1_D' in response.data)
        self.assertTrue(b'MCQ_Qn1_Ans' in response.data)
        self.assertTrue(b'MCQ_Qn1_Score' in response.data)
     

    # Check for Data returned
    def test_quiz_details(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_qn_ans")
        response_body = json.loads(response.data)
        self.assertEqual('C101-L1-Quiz', response_body['data'][0]['quiz_qn_id'])
        self.assertEqual('What is the  lesson?', response_body['data'][0]['MCQ_Qn1'])
        self.assertEqual('SPM', response_body['data'][0]['MCQ_Qn1_A'])
        self.assertEqual('ESM', response_body['data'][0]['MCQ_Qn1_B'])
        self.assertEqual('ESD', response_body['data'][0]['MCQ_Qn1_C'])
        self.assertEqual('WAD2', response_body['data'][0]['MCQ_Qn1_D'])
        self.assertEqual('SPM', response_body['data'][0]['MCQ_Qn1_Ans'])
        self.assertEqual(1, response_body['data'][0]['MCQ_Qn1_Score'])

        self.assertEqual('What is the most favourite color?', response_body['data'][0]['MCQ_Qn2'])
        self.assertEqual('red', response_body['data'][0]['MCQ_Qn2_A'])
        self.assertEqual('pink', response_body['data'][0]['MCQ_Qn2_B'])
        self.assertEqual('yellow', response_body['data'][0]['MCQ_Qn2_C'])
        self.assertEqual('blue', response_body['data'][0]['MCQ_Qn2_D'])
        self.assertEqual('blue', response_body['data'][0]['MCQ_Qn2_Ans'])
        self.assertEqual(1, response_body['data'][0]['MCQ_Qn2_Score'])

        self.assertEqual('I like starbucks?', response_body['data'][0]['TandF_Qn1'])
        self.assertEqual('True', response_body['data'][0]['TandF_Qn1_Ans'])
        self.assertEqual(1, response_body['data'][0]['TandF_Qn1_Score'])
        self.assertEqual('I do not like strabucks?', response_body['data'][0]['TandF_Qn2'])
        self.assertEqual('False', response_body['data'][0]['TandF_Qn2_Ans'])
        self.assertEqual(1, response_body['data'][0]['TandF_Qn2_Score'])


################################################# Done by Goh Xue Qi #################################################
# Test if API '/quiz_take' works
class Test_Quiz_take(unittest.TestCase):
    # Check if response is 200
    def test_quiz_take(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_take")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_quiz_take(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_take")
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the quiz take Details required are Present
    def test_quiz_take_details(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_take")
        self.assertTrue(b'quiz_take_id' in response.data)
        self.assertTrue(b'quiz_score' in response.data)
       
 

    # Check for Data returned
    def test_quiz_take_details(self):
        tester = app.test_client(self)
        response = tester.get("/quiz_take")
        response_body = json.loads(response.data)
        self.assertEqual('001-C101-L1', response_body['data'][0]['quiz_take_id'])
        self.assertEqual(2, response_body['data'][0]['quiz_score'])
      


    # CHECK CONTENT OF POST METHOD
    def test_take_quiz_post(data):       
        response = app.test_client().post(
        '/quiz_take',
        data=json.dumps({'quiz_take_id': '002-C101-L3', 'quiz_score':'4'}),
        content_type='application/json',
    )
        response = json.loads(response.get_data(data))

        data.assertEqual('002-C101-L3', response['quiz_take_id'])
        data.assertEqual(4, response['quiz_score'])
      
       



if __name__ == '__main__':
    unittest.main()
