import unittest
from Courses import *

# Created by Mayuri Salunke
class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course1 = Course(course_id='E201', course_name='Intermediate Mathematics', course_type='Biddable', course_prerequisite='E101', course_brief='This is a Year1 course which requires the completion of E101 Basic Mathematics', total_slots_available=80, course_period='Term2', FK_trainer_course_section_id='E201G1, E201G2', FK_quiz_id='A201')

    def test_to_dict(self):
        self.assertEqual(self.course1.to_dict(), {
            'course_id': 'E201',
            'course_name': 'Intermediate Mathematics',
            'course_type': 'Biddable',
            'course_prerequisite': 'E101',
            'course_brief': 'This is a Year1 course which requires the completion of E101 Basic Mathematics',
            'total_slots_available': 80,
            'course_period': 'Term2',
            'FK_trainer_course_section_id': 'E201G1, E201G2',
            'FK_quiz_id': 'A201'
            }
        )
    
    def test_getFunctions(self):
        self.assertEqual(self.course1.get_CourseID(), 'E201')
        self.assertEqual(self.course1.get_CourseName(), 'Intermediate Mathematics')
        self.assertEqual(self.course1.get_CourseType(), 'Biddable')
        self.assertEqual(self.course1.get_CoursePrerequisite(), 'E101')
        self.assertEqual(self.course1.get_CourseBrief(), 'This is a Year1 course which requires the completion of E101 Basic Mathematics')
        self.assertEqual(self.course1.get_CourseSlotsAvail(), 80)
        self.assertEqual(self.course1.get_CoursePeriod(), 'Term2')
        self.assertEqual(self.course1.get_CourseTrainerCourseSectionID(), 'E201G1, E201G2')
        self.assertEqual(self.course1.get_CourseQuizID(), 'A201')
        


if __name__ == "__main__":
    unittest.main()