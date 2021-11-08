
import unittest
import json

from werkzeug import Response, test
from Enrollment import Enrollment,app,db


#######################################################Done by Sun Yuyang###########################################


class TestEnroll(unittest.TestCase):
    test1 = Enrollment(enrollment_id='1', engineer_id='001', course_id='C101', course_class_id='C101-C1')
    def test_to_dict(self):
        self.assertEqual(self.test1.to_dict(), {
            'enrollment_id': '1',
            'engineer_id': '001',
            'course_id': 'C101',
            'course_class_id': 'C101-C1'
        }
        )
    

    ###check if the course id in course_class_id and the course_id match#####
    def test_course_id(self):
        course_id = self.test1.to_dict()['course_class_id'].split('-')[0]
        inserted_course_id = self.test1.to_dict()['course_id']
        self.assertEqual(course_id, inserted_course_id)
    

if __name__ == '__main__':
    unittest.main()







