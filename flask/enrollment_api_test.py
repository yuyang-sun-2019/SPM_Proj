
import unittest
import json


from werkzeug import Response, test
from Enrollment import Enrollment,app,db

#######################################################Done by Sun Yuyang###########################################


   ###################Testing App route in enrollment##################

    ######APP ROUTE /enrollment##########
class TestEnroll_route(unittest.TestCase):
    # IF STATUS CODE=200
    def test_enroll_200(self):
        test2 = app.test_client(self)
        data = test2.get("/enrollment")
        statuscode = data.status_code
        self.assertEqual(statuscode,200)
    
    # IF RESULT RETURNED IN IS JSON
    def test_enroll_json(self):
        test2 = app.test_client(self)
        data = test2.get("/enrollment")
        self.assertEqual(data.content_type, "application/json")


    # # CHECK CONTENT OF GET METHOD
    def test_enrollment_get(self):
        test2 = app.test_client(self)
        data =test2.get("/enrollment")
        data_content = json.loads(data.data)
        self.assertEqual(1, data_content['data'][0]['enrollment_id'])
        self.assertEqual(1, data_content['data'][0]['engineer_id'])
        self.assertEqual('C205', data_content['data'][0]['course_id'])
        self.assertEqual('C205-C1', data_content['data'][0]['course_class_id'])
    

######METHOD=POST##################

    # CHECK CONTENT OF POST METHOD
    def test_enrollment_post(data):       
        response = app.test_client().post(
        '/enrollment',
        data=json.dumps({'engineer_id': '1', 'course_id':'C101','course_class_id':'C101-C1'}),
        content_type='application/json',
    )
        response = json.loads(response.get_data(data))

        data.assertEqual(1, response['engineer_id'])
        data.assertEqual('C101', response['course_id'])
        data.assertEqual('C101-C1', response['course_class_id'])

    

if __name__ == '__main__':
    unittest.main()

