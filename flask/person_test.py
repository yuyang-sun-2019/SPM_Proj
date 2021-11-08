
import unittest
import json

from werkzeug import Response, test
from Person import Person,Engineer,Trainers,HR,app,db


#######################################################Done by Soh Keyang###########################################


class TestPerson(unittest.TestCase):
    test1 = Person(id='1', name='Ally', email = "ally@engineer.com", pwd='engineer001')
    def test_to_dict(self):
        self.assertEqual(self.test1.to_dict(), {
            'id': '1',
            'name': 'Ally',
            'email': 'ally@engineer.com',
            'pwd' : 'engineer001'
        }
        )
    

    ###check if the person id is an integer#####
    def test_person_id(self):
        self.assertTrue(type(int(self.test1.to_dict()['id'])) == int)
    

    ###Check if email format is proper and has @###
    def test_person_email(self):
        self.assertIn('@', self.test1.to_dict()['email'])

class TestEngineer(unittest.TestCase):
    engineer1 = Engineer(engineer_id = '1', engineer_completed_courses = 'C101-C1, C102-C2, C103-C2', engineer_inprogress_courses = 'C201-C2, C202-C1, C104-C1')
    def test_to_dict(self):
        self.assertEqual(self.engineer1.to_dict(), {
            'engineer_id' : '1',
            'engineer_completed_courses' : 'C101-C1, C102-C2, C103-C2',
            'engineer_inprogress_courses' : 'C201-C2, C202-C1, C104-C1'
        }
        ) 
    ##Test courses format, should match courses DB##
    def test_courses(self):
        self.assertTrue(len(self.engineer1.to_dict()['engineer_completed_courses'].split(',')[0]) == 7)
        self.assertTrue(len(self.engineer1.to_dict()['engineer_inprogress_courses'].split(',')[0]) == 7)
    ###Check if engineer id is integer###
    def test_engineer_id(self):
        self.assertTrue(type(int(self.engineer1.to_dict()['engineer_id'])) == int)

class TestTrainers(unittest.TestCase):
    trainer1 = Trainers(trainer_id = '761', trainer_course_class_id = 'C101-C1, C101-C2, C101-C3, C102-C1, C102-C2, C102-C3, C201-C1, C201-C2, C202-C1, C202-C2, C301-C1, C301-C2, C301-C3, C302-C1, C302-C2, C302-C3')
    def test_to_dict(self):
        self.assertEqual(self.trainer1.to_dict(), {
            'trainer_id' : '761',
            'trainer_course_class_id' : 'C101-C1, C101-C2, C101-C3, C102-C1, C102-C2, C102-C3, C201-C1, C201-C2, C202-C1, C202-C2, C301-C1, C301-C2, C301-C3, C302-C1, C302-C2, C302-C3',
        }
        ) 
    ### Check if trainer id is integer ###
    def test_trainers_id(self):
        self.assertTrue(type(int(self.trainer1.to_dict()['trainer_id'])) == int)

    ##Test courses format, should match courses DB##
    def test_courses(self):
        self.assertTrue(len(self.trainer1.to_dict()['trainer_course_class_id'].split(',')[0]) == 7)

class TestHR(unittest.TestCase):
    hr1 = HR(hr_id = '366',  courses_assigned = 'C101, C102, C103, C104, C105, C305')
    def test_to_dict(self):
        self.assertEqual(self.hr1.to_dict(), {
            'hr_id' : '366',
            'courses_assigned' : 'C101, C102, C103, C104, C105, C305',
        }
        ) 
    ### Check if hr id is integer ###
    def test_hr_id(self):
        self.assertTrue(type(int(self.hr1.to_dict()['hr_id'])) == int)
    ##Test courses format, should match courses DB##
    def test_courses(self):
        self.assertTrue(len(self.hr1.to_dict()['courses_assigned'].split(',')[0]) == 4)

if __name__ == '__main__':
    unittest.main()







