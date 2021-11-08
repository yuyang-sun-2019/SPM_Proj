import unittest
import json

from Courses import app, db, Course, Course_Class, Course_Lesson


################################################# Done by MAYURI MILIND SALUNKE #################################################
# Test if API '/course' works
class Test_Course(unittest.TestCase):
    # Check if response is 200
    def test_course(self):
        tester = app.test_client(self)
        response = tester.get("/course")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_course(self):
        tester = app.test_client(self)
        response = tester.get("/course")
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the Course Details requires are Present
    def test_course_details(self):
        tester = app.test_client(self)
        response = tester.get("/course")
        self.assertTrue(b'course_id' in response.data)
        self.assertTrue(b'course_name' in response.data)
        self.assertTrue(b'course_type' in response.data)
        self.assertTrue(b'course_prerequisite' in response.data)
        self.assertTrue(b'course_brief' in response.data)
        self.assertTrue(b'course_class' in response.data)
        self.assertTrue(b'lessons' in response.data)
        self.assertTrue(b'start_date' in response.data)
        self.assertTrue(b'end_date' in response.data)

    # Check for Data returned
    def test_course_details(self):
        tester = app.test_client(self)
        response = tester.get("/course")
        response_body = json.loads(response.data)
        self.assertEqual('C101', response_body['data'][0]['course_id'])
        self.assertEqual('C101-C1, C101-C2, C101-C3', response_body['data'][0]['course_class'])
        self.assertEqual('Basic Mathematics', response_body['data'][0]['course_name'])
        self.assertEqual('Assigned', response_body['data'][0]['course_type'])



# Test if API '/course/course_id' works
class Test_Course(unittest.TestCase):
    # Check if response is 200
    def test_course(self):
        tester = app.test_client(self)
        course_id = 'C101'
        response = tester.get("/course/"+course_id)
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_course(self):
        tester = app.test_client(self)
        course_id = 'C101'
        response = tester.get("/course/"+course_id)
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the Course Details requires are Present
    def test_course_details(self):
        tester = app.test_client(self)
        course_id = 'C101'
        response = tester.get("/course/"+course_id)
        self.assertTrue(b'course_id' in response.data)
        self.assertTrue(b'course_name' in response.data)
        self.assertTrue(b'course_type' in response.data)
        self.assertTrue(b'course_prerequisite' in response.data)
        self.assertTrue(b'course_brief' in response.data)
        self.assertTrue(b'course_class' in response.data)
        self.assertTrue(b'lessons' in response.data)
        self.assertTrue(b'start_date' in response.data)
        self.assertTrue(b'end_date' in response.data)

    # Check for Data returned
    def test_course_details(self):
        tester = app.test_client(self)
        course_id = 'C101'
        response = tester.get("/course/"+course_id)
        response_body = json.loads(response.data)
        self.assertEqual('C101', response_body['data']['course_id'])
        self.assertEqual('C101-C1, C101-C2, C101-C3', response_body['data']['course_class'])
        self.assertEqual('Basic Mathematics', response_body['data']['course_name'])
        self.assertEqual('Assigned', response_body['data']['course_type'])








################################################# Done by MAYURI MILIND SALUNKE #################################################
# Test if API '/course_class' works
class Test_Course(unittest.TestCase):
    # Check if response is 200
    def test_course(self):
        tester = app.test_client(self)
        response = tester.get("/course_class")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_course(self):
        tester = app.test_client(self)
        response = tester.get("/course_class")
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the Course Details requires are Present
    def test_course_details(self):
        tester = app.test_client(self)
        response = tester.get("/course_class")
        self.assertTrue(b'course_id' in response.data)
        self.assertTrue(b'course_class_id' in response.data)
        self.assertTrue(b'seats_available' in response.data)
     

    # Check for Data returned
    def test_course_details(self):
        tester = app.test_client(self)
        response = tester.get("/course_class")
        response_body = json.loads(response.data)
        self.assertEqual('C101', response_body['data'][0]['course_id'])
        self.assertEqual('C101-C1', response_body['data'][0]['course_class_id'])
        self.assertEqual(20, response_body['data'][0]['seats_available'])



# Test if API '/course_class/course_class_id' works
class Test_Course(unittest.TestCase):
    # Check if response is 200
    def test_course(self):
        tester = app.test_client(self)
        course_class_id = 'C101-C1'
        response = tester.get("/course_class/"+course_class_id)
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_course(self):
        tester = app.test_client(self)
        course_class_id = 'C101-C1'
        response = tester.get("/course_class/"+course_class_id)
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the Course Details requires are Present
    def test_course_details(self):
        tester = app.test_client(self)
        course_class_id = 'C101-C1'
        response = tester.get("/course_class/"+course_class_id)
        self.assertTrue(b'course_id' in response.data)
        self.assertTrue(b'course_class_id' in response.data)
        self.assertTrue(b'seats_available' in response.data)

    # Check for Data returned
    def test_course_details(self):
        tester = app.test_client(self)
        course_class_id = 'C101-C1'
        response = tester.get("/course_class/"+course_class_id)
        response_body = json.loads(response.data)
        self.assertEqual('C101', response_body['data']['course_id'])
        self.assertEqual('C101-C1', response_body['data']['course_class_id'])
        self.assertEqual(20, response_body['data']['seats_available'])








################################################# Done by MAYURI MILIND SALUNKE #################################################
# Test if API '/course_lesson' works
class Test_Course(unittest.TestCase):
    # Check if response is 200
    def test_course(self):
        tester = app.test_client(self)
        response = tester.get("/course_lesson")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_course(self):
        tester = app.test_client(self)
        response = tester.get("/course_lesson")
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the Course Details requires are Present
    def test_course_details(self):
        tester = app.test_client(self)
        response = tester.get("/course_lesson")
        self.assertTrue(b'course_id' in response.data)
        self.assertTrue(b'course_lesson_id' in response.data)
        self.assertTrue(b'doc_material' in response.data)
        self.assertTrue(b'pdf_material' in response.data)
        self.assertTrue(b'ppt_material' in response.data)
        self.assertTrue(b'quiz_id' in response.data)
        self.assertTrue(b'video_material' in response.data)
 

    # Check for Data returned
    def test_course_details(self):
        tester = app.test_client(self)
        response = tester.get("/course_lesson")
        response_body = json.loads(response.data)
        self.assertEqual('C101', response_body['data'][0]['course_id'])
        self.assertEqual('C101-L1', response_body['data'][0]['course_lesson_id'])
        self.assertEqual('doc1.docx, doc2.docx, doc3.docx', response_body['data'][0]['doc_material'])
        self.assertEqual('pdf1.pdf, pdf2.pdf', response_body['data'][0]['pdf_material'])
        self.assertEqual('ppt1.pptx, ppt2.pptx', response_body['data'][0]['ppt_material'])
        self.assertEqual(None, response_body['data'][0]['quiz_id'])
        self.assertEqual('vid1.mp4, vid2.mp4, vid3.mp4', response_body['data'][0]['video_material'])




# Test if API '/course_lesson/course_id' works
class Test_Course(unittest.TestCase):
    # Check if response is 200
    def test_course(self):
        tester = app.test_client(self)
        course_lesson_id = 'C101-L1'
        response = tester.get("/course_lesson/"+course_lesson_id)
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    # Check if content return is application/json
    def test_course(self):
        tester = app.test_client(self)
        course_lesson_id = 'C101-L1'
        response = tester.get("/course_lesson/"+course_lesson_id)
        self.assertEqual(response.content_type, "application/json")
        
    # Check if all the Course Details requires are Present
    def test_course_details(self):
        tester = app.test_client(self)
        course_lesson_id = 'C101-L1'
        response = tester.get("/course_lesson/"+course_lesson_id)
        self.assertTrue(b'course_id' in response.data)
        self.assertTrue(b'course_lesson_id' in response.data)
        self.assertTrue(b'doc_material' in response.data)
        self.assertTrue(b'pdf_material' in response.data)
        self.assertTrue(b'ppt_material' in response.data)
        self.assertTrue(b'quiz_id' in response.data)
        self.assertTrue(b'video_material' in response.data)

    # Check for Data returned
    def test_course_details(self):
        tester = app.test_client(self)
        course_lesson_id = 'C101-L1'
        response = tester.get("/course_lesson/"+course_lesson_id)
        response_body = json.loads(response.data)
        self.assertEqual('C101', response_body['data']['course_id'])
        self.assertEqual('C101-L1', response_body['data']['course_lesson_id'])
        self.assertEqual('doc1.docx, doc2.docx, doc3.docx', response_body['data']['doc_material'])
        self.assertEqual('pdf1.pdf, pdf2.pdf', response_body['data']['pdf_material'])
        self.assertEqual('ppt1.pptx, ppt2.pptx', response_body['data']['ppt_material'])
        self.assertEqual(None, response_body['data']['quiz_id'])
        self.assertEqual('vid1.mp4, vid2.mp4, vid3.mp4', response_body['data']['video_material'])





if __name__ == '__main__':
    unittest.main()
