import unittest
import json
from Courses import Course, Course_Progress,app,db


################### Testing App route in course_progress ##################

####################### APP ROUTE /course_progress ##########

######################### METHOD=POST #########################

class Test_Progress_route(unittest.TestCase):

    # Check if data is 200
    def test_course_progress(self):
        test5 = app.test_client(self)
        progress_id = '2 C201-C1'
        data = test5.get("/course_progress/"+progress_id)
        statuscode = data.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_course_progress(self):
        test5 = app.test_client(self)
        progress_id = '2 C201-C1'
        data = test5.get("/course_progress/"+progress_id)
        content_type = data.content_type
        self.assertEqual(content_type, "application/json")
        
    # Check if all the Course Details requires are Present
    def test_course_progress_details(self):
        test5 = app.test_client(self)
        progress_id = '2 C201-C1'
        data = test5.get("/course_progress/"+progress_id)
        self.assertTrue(b'engineer_id' in data.data)
        self.assertTrue(b'course_id' in data.data)
        self.assertTrue(b'lesson' in data.data)
        self.assertTrue(b'doc_material' in data.data)
        self.assertTrue(b'pdf_material' in data.data)
        self.assertTrue(b'ppt_material' in data.data)
        self.assertTrue(b'quiz_id' in data.data)
        self.assertTrue(b'video_material' in data.data)

    # Check for Data returned
    def test_course_progress_details(self):
        test5 = app.test_client(self)
        progress_id = '2 C201-C1'
        data = test5.get("/course_progress/"+progress_id)
        data_body = json.loads(data.data)
        self.assertEqual(2, data_body['data']['engineer_id'])
        self.assertEqual('C201', data_body['data']['course_id'])
        self.assertEqual('C201-L1',data_body['data']['lesson'])


if __name__ == '__main__':
    unittest.main()
